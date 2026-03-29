# Operator

Operator protocol and built-in implementations for composable computation in hypergraph workflows. This library defines the core `Operator` behaviour and provides common operator types for building complex agent workflows.

## Overview

The Operator library provides:
- **Operator protocol**: Simple callback-based interface (`call/1`) for all operators
- **MapOperator**: Transform input values
- **SequenceOperator**: Chain operators together sequentially
- **ParallelOperator**: Execute operators in parallel and merge results
- **LLMOperator**: Stub implementation for language model integration

## Built-in Operators

### MapOperator
Applies a function to input and returns transformed output.

### SequenceOperator
Executes operators in order, passing outputs from one to the next.

### ParallelOperator
Executes multiple operators concurrently and merges their outputs.

### LLMOperator
Formats prompts and executes language model calls (currently stubbed for demonstration).

## Installation

If [available in Hex](https://hex.pm/docs/publish), the package can be installed
by adding `operator` to your list of dependencies in `mix.exs`:

```elixir
def deps do
  [
    {:operator, "~> 0.1.0"}
  ]
end
```

Documentation can be generated with [ExDoc](https://github.com/elixir-lang/ex_doc)
and published on [HexDocs](https://hexdocs.pm). Once published, the docs can
be found at <https://hexdocs.pm/operator>.

