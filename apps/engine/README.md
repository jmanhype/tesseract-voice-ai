# Engine

Hypergraph execution engine for multi-agent workflows. This library provides graph-based operator execution with dependency resolution, topological sorting, and support for both sequential and parallel execution modes.

## Overview

The Engine provides:
- **Graph execution**: Run DAGs (Directed Acyclic Graphs) of operators with automatic dependency resolution
- **Topological sorting**: Automatically determines correct execution order based on dependencies
- **Parallel execution**: Execute independent nodes concurrently using Elixir tasks
- **Input/output validation**: Optional specification-based validation for operators
- **Type safety**: Comprehensive typespecs for all public functions

## Usage

```elixir
# Define a simple graph
graph = %{
  :node1 => %{operator: MyOperator, deps: []},
  :node2 => %{operator: AnotherOperator, deps: [:node1]}
}

# Run sequentially
Engine.run(graph, %{input: "data"}, mode: :sequential)

# Run in parallel
Engine.run(graph, %{input: "data"}, mode: :parallel)
```

## Installation

If [available in Hex](https://hex.pm/docs/publish), the package can be installed
by adding `engine` to your list of dependencies in `mix.exs`:

```elixir
def deps do
  [
    {:engine, "~> 0.1.0"}
  ]
end
```

Documentation can be generated with [ExDoc](https://github.com/elixir-lang/ex_doc)
and published on [HexDocs](https://hexdocs.pm). Once published, the docs can
be found at <https://hexdocs.pm/engine>.

