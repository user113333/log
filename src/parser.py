BOOLEAN_LITERALS = {"TRUE": True, "FALSE": False}
OPERATORS = {"AND", "OR"}

def parse(tokens):
    if len(tokens) == 1:
        literal = tokens[0]
        if literal in BOOLEAN_LITERALS:
            return None, BOOLEAN_LITERALS[literal]

    if len(tokens) == 3:
        left, operator, right = tokens
        if (
            left in BOOLEAN_LITERALS
            and operator in OPERATORS
            and right in BOOLEAN_LITERALS
        ):
            return None, (operator, BOOLEAN_LITERALS[left], BOOLEAN_LITERALS[right])

    return "Invalid expression", None
