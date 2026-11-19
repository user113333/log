# LogicLang

LogicLang is a small programming language written in Python for working with Boolean expressions and discrete mathematics.

The goal of this project is to learn how programming languages are designed and implemented by building one from scratch.

## Goals

The language will be developed step by step:

1. Evaluate Boolean expressions (`AND`, `OR`, `NOT`, `XOR`).
2. Support variables and more complex expressions.
3. Generate truth tables.
4. Check logical equivalence.
5. Implement a SAT solver.
6. Explore additional discrete mathematics features.

## Project Structure

```text
logiclang/
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
