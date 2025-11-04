from fastapi import FastAPI, Request, Response
from fastapi.responses import StreamingResponse, JSONResponse
from typing import AsyncGenerator, Dict, Any
import asyncio

app = FastAPI(title="Minimal Python A2A Agent")

AGENT_CARD: Dict[str, Any] = {
    "id": "pyagent1",
    "name": "Python Agent",
    "version": "0.1.0",
    "description": "Minimal Python A2A agent",
    "capabilities": ["task_request", "agent_discovery"],
    "endpoints": {"a2a": "/api/a2a", "agent_card": "/api/agent_card"},
    "authentication": None
}

@app.get("/api/agent_card")
def get_agent_card() -> Dict[str, Any]:
    """
    Return this agent's card for discovery.

    Returns:
        Dict containing agent metadata including id, name, version, capabilities, and endpoints.
    """
    return AGENT_CARD

@app.post("/api/agent_card")
def register_agent_card(card: Dict[str, Any]) -> Dict[str, Any]:
    """
    Accept and echo agent card registration (stub for demo).

    Args:
        card: Agent card dictionary containing registration information.

    Returns:
        Dict with status and echoed card data.
    """
    return {"status": "ok", "card": card}

async def stream_task_progress() -> AsyncGenerator[bytes, None]:
    """
    Simulate streaming task progress events.

    Yields:
        Encoded JSON progress updates followed by final result.
    """
    for i in range(5):
        yield (f'{ {"type": "task_progress", "progress": i*20} }\n').encode()
        await asyncio.sleep(0.5)
    yield b'{"type": "result", "payload": {"result": "done"}}\n'

@app.post("/api/a2a")
async def a2a_endpoint(request: Request) -> JSONResponse | StreamingResponse:
    """
    Accept A2A messages and stream responses if requested.

    Handles task_request, task_chunk, agent_event, and error cases.
    Supports streaming for task_request and task_chunk message types.

    Args:
        request: FastAPI Request object containing A2A message in JSON format.

    Returns:
        Either a JSONResponse for immediate responses or StreamingResponse for streaming data.
        Returns 400 error for invalid message format.
    """
    body = await request.json()
    # Strict error check FIRST
    if "type" not in body or not isinstance(body.get("type"), str):
        print(f"[error] Missing or invalid 'type' field in message: {body}")
        return JSONResponse({"status": "error", "error": "Missing or invalid 'type' field"}, status_code=400)
    msg_type = body["type"]
    payload = body.get("payload", {})

    # Streaming for task_request
    if msg_type == "task_request" and payload.get("stream", False):
        return StreamingResponse(stream_task_progress(), media_type="application/json")
    # Always stream for task_chunk (even if no stream param)
    if msg_type == "task_chunk":
        async def chunk_stream():
            for i in range(3):
                chunk = {"type": "task_chunk", "chunk": f"partial_{i}"}
                yield (f"{chunk}\n").encode()
                await asyncio.sleep(0.3)
            result = {"type": "result", "payload": {"result": "final from chunk"}}
            yield (f"{result}\n").encode()
        return StreamingResponse(chunk_stream(), media_type="application/json")
    if msg_type == "agent_event":
        # Log and acknowledge
        print(f"[agent_event] {payload}")
        return JSONResponse({"status": "ok", "type": "agent_event", "event": payload})
    # Default: echo
    return JSONResponse({"status": "ok", "type": msg_type, "echo": body})
