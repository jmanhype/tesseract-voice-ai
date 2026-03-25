# Hypergraph Agents Umbrella

Multi-language agent framework for distributed workflows using the A2A (Agent-to-Agent) protocol. Elixir/Phoenix on the orchestration side, Python/FastAPI for interop agents. NATS for event streaming, Prometheus + Grafana for observability.

> **Note:** This repository is named `tesseract-voice-ai` but the actual codebase is the Hypergraph Agents platform. A voice-AI project exists only as scaffolding inside `Downloads/tesseract-voice-ai/` and is not wired into the main application.

## Status

The Elixir A2A agent, Python minimal agent, event bus, agent registry, workflow operators, and Prometheus metrics endpoint all have passing tests. The voice-AI subsystem in `Downloads/` is a design document with frontend stubs, not a working system.

## What it does

- **A2A protocol**: Agents exchange typed JSON messages (`task_request`, `result`, `status_update`, `agent_discovery`, `negotiation`) over HTTP.
- **Agent registry**: Agents register by exchanging agent cards via `GET/POST /api/agent_card`.
- **Event streaming**: NATS pub/sub for async event delivery between Elixir and Python agents.
- **Workflow engine**: Graph-based execution with sequence, parallel, branch, map, aggregate, and LLM operators.
- **Observability**: Prometheus `/metrics` endpoint, Grafana dashboards, structured logging via GoldRush.

## Architecture

| Component | Stack | Location |
|---|---|---|
| A2A Agent (main) | Elixir/Phoenix | `apps/a2a_agent_web/` |
| Workflow engine | Elixir | `apps/engine/` |
| Hypergraph orchestrator | Elixir | `apps/hypergraph_agent/` |
| Operator library | Elixir | `apps/operator/` |
| Python A2A agent | FastAPI | `agents/python_agents/minimal_a2a_agent/` |
| Config/Infra | Docker Compose, NATS, Prometheus, Grafana | `config/`, `docker-compose.yml` |

## Requirements

| Requirement | Version |
|---|---|
| Elixir | 1.16+ |
| Erlang/OTP | 26+ |
| Python | 3.10+ |
| Docker + Compose | For full stack |
| NATS | Provided via Docker Compose |

## Quick start

### Full stack (Docker)

```sh
make up          # starts Elixir agent, Python agent, NATS, Prometheus, Grafana
make test        # runs Elixir + Python tests
make down        # stops everything
```

### Manual

Elixir agent:
```sh
cd apps/a2a_agent_web
mix deps.get
mix phx.server   # http://localhost:4000
```

Python agent:
```sh
cd agents/python_agents/minimal_a2a_agent
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 5001
```

## A2A message schema

| Field | Type | Required | Description |
|---|---|---|---|
| type | string | Yes | `task_request`, `result`, `status_update`, `agent_discovery`, `negotiation` |
| sender | string | Yes | Agent ID |
| recipient | string | Yes | Target agent ID |
| payload | object | Yes | Message-specific data |
| task_id | string | No | Task identifier |
| timestamp | string | No | ISO 8601 |

### Endpoints

- `GET /api/agent_card` -- returns agent metadata
- `POST /api/a2a` -- receives an A2A message, validates, routes to handler
- `GET /metrics` -- Prometheus metrics

## Observability

Prometheus scrapes both agents. Grafana is available at `http://localhost:3000` (default `admin`/`admin`). Key metrics:

- `a2a_messages_total{type=...}` -- messages received by type
- `a2a_orchestrations_total` -- workflow executions
- `a2a_errors_total` -- error responses

## Project structure

```
apps/
  a2a_agent_web/      Phoenix A2A agent (controllers, event bus, operators, metrics)
  engine/             Workflow execution engine
  hypergraph_agent/   Orchestrator + sample agent
  operator/           Operator specs and implementations
agents/
  python_agents/
    minimal_a2a_agent/  FastAPI A2A agent for interop testing
config/               Elixir config, Prometheus config
hg_project/           Duplicate of the umbrella (appears to be a snapshot)
Downloads/            Voice-AI scaffolding (not integrated)
```

## Limitations

- The repository name does not match its contents. It is an agent orchestration framework, not a voice-AI system.
- `hg_project/` is a near-complete duplicate of the root project.
- `Downloads/corpus-mlx/` contains ~200 unrelated image-generation artifacts (~MLX diffusion experiments).
- `Downloads/tesseract-voice-ai/` has frontend stubs and a GraphQL schema but no working backend.
- `.venv/` is committed to git.
- The `negotiation` and `agent_discovery` A2A message types return stub responses.
- No integration tests that exercise the full NATS event loop end-to-end.

## License

MIT
