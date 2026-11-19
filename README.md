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

## Interpreter Cheatsheet

An **interpreter** is a program that reads and executes code written in another programming language.

LogicLang uses the following structure:

```text
Source Code
    |
    v
  Lexer
    |
    v
  Tokens
    |
    v
  Parser
    |
    v
   AST
    |
    v
 Evaluator
    |
    v
  Result
```

### 1. Lexer (Tokenizer)

The lexer reads the source code character by character and converts it into **tokens**.

Tokens are the smallest meaningful elements of the language.

**Input:**
```text
TRUE AND FALSE
```

**Output:**
```text
[
    TRUE,
    AND,
    FALSE
]
```

The lexer recognizes keywords, operators, parentheses, and other symbols. It does not evaluate expressions.

### 2. Parser

The parser takes the tokens and checks whether they follow the language's **grammar rules**.

It determines how the expression is structured, taking operator precedence and parentheses into account.

**Input:**
```text
[TRUE, AND, FALSE]
```

**Output:** An Abstract Syntax Tree (AST).

### 3. AST (Abstract Syntax Tree)

An AST is a tree representation of the expression.

For example, `TRUE AND FALSE` becomes:

```text
      AND
     /   \
   TRUE  FALSE
```

Each node represents an operation or a value.

More complex example:

```text
TRUE OR FALSE AND TRUE
```

Becomes:

```text
        OR
       /  \
     TRUE  AND
          /   \
        FALSE TRUE
```

The AST preserves the structure of the expression and makes it easier to evaluate or analyze.

### 4. Evaluator

The evaluator walks through the AST and computes the result.

For example:

```text
      AND
     /   \
   TRUE  FALSE
```

It evaluates the children and then applies the `AND` operation:

```text
TRUE AND FALSE = FALSE
```

The evaluator can later be extended to support variables, functions, and other operations.

### 5. REPL (Read–Eval–Print Loop)

The REPL provides an interactive way to use the language.

It repeatedly:

1. **Reads** an expression from the user.
2. **Evaluates** it using the interpreter.
3. **Prints** the result.
4. **Loops** back to wait for another expression.

Example:

```text
> TRUE AND FALSE
FALSE

> NOT FALSE
TRUE

> TRUE XOR TRUE
FALSE
```

### 6. Grammar

The grammar defines which expressions are valid in the language.

It describes the syntax and operator precedence.

For example:

```ebnf
expression = or_expr ;
or_expr    = and_expr, { "OR", and_expr } ;
and_expr   = primary, { "AND", primary } ;
primary    = "TRUE" | "FALSE" | "(", expression, ")" ;
```

This simplified grammar supports `AND`, `OR`, and parentheses. Other operators will be added later.

The **parser uses the grammar** to understand the structure of the tokens.

### Summary

| Component | Responsibility |
|---|---|
| Lexer | Characters → Tokens |
| Parser | Tokens → AST |
| AST | Represents the expression as a tree |
| Evaluator | AST → Result |
| REPL | Interactive interface |
| Grammar | Defines valid syntax and structure |

**Key idea:** Each component has one responsibility. Keeping them separate makes the interpreter easier to understand, test, and extend.

Later, features such as truth tables, logical equivalence checking, and SAT solving can reuse the same AST without needing a completely new lexer or parser.

## Planned project structure

### Intended file layout

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
