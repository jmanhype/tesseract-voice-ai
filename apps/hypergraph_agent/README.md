# HypergraphAgent

Multi-agent protocol and behaviour specification for the hypergraph agent system. This library defines the core `HypergraphAgent` behaviour that all agents must implement, along with a reference `BasicAgent` implementation.

## Overview

HypergraphAgent provides:
- A simple callback-based protocol for agent implementations
- Type specifications for agent input/output
- A reference `BasicAgent` implementation demonstrating the behaviour

Agents implementing this behaviour can participate in multi-agent workflows orchestrated by the Engine.

## Installation

If [available in Hex](https://hex.pm/docs/publish), the package can be installed
by adding `hypergraph_agent` to your list of dependencies in `mix.exs`:

```elixir
def deps do
  [
    {:hypergraph_agent, "~> 0.1.0"}
  ]
end
```

Documentation can be generated with [ExDoc](https://github.com/elixir-lang/ex_doc)
and published on [HexDocs](https://hexdocs.pm). Once published, the docs can
be found at <https://hexdocs.pm/hypergraph_agent>.

