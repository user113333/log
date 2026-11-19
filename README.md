# Log

Log is a small programming language for Boolean expressions and discrete mathematics, built as a learning project in Python.

The goal of this project is to learn how programming languages are designed and implemented by building one from scratch.

## Goals

The language will be developed step by step:

1. Evaluate the expressions in the current grammar, then add negation and exclusive or.
2. Support variables and more complex expressions.
3. Generate truth tables.
4. Check logical equivalence.
5. Implement a SAT solver.
6. Explore additional discrete mathematics features.

## Planned project structure

The [grammar](docs/grammar.md) documents the language, and [`src/main.py`](src/main.py) is a starter script. The tree below shows the intended layout.

```text
log/
├── README.md
├── AGENTS.md
├── pyproject.toml
├── src/
│   ├── __init__.py
│   ├── tokens.py       # Token definitions
│   ├── lexer.py        # Converts text into tokens
│   ├── parser.py       # Builds an abstract syntax tree
│   ├── ast_nodes.py    # AST node definitions
│   ├── evaluator.py    # Evaluates expressions
│   └── repl.py         # Interactive calculator
├── tests/
│   ├── test_lexer.py
│   ├── test_parser.py
│   └── test_evaluator.py
└── docs/
    ├── grammar.md         # Language syntax and rules
    └── roadmap.md         # Future development plans
```
