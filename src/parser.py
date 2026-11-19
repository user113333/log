BOOLEAN_LITERALS = {"TRUE": True, "FALSE": False}
OPERATORS = {"AND", "OR"}


def parse(tokens):
    if len(tokens) == 1:
        literal_token = tokens[0]
        if literal_token in BOOLEAN_LITERALS:
            return None, BOOLEAN_LITERALS[literal_token]

    if len(tokens) == 3:
        left_token, operator, right_token = tokens
        if (
            left_token in BOOLEAN_LITERALS
            and operator in OPERATORS
            and right_token in BOOLEAN_LITERALS
        ):
            left = BOOLEAN_LITERALS[left_token]
            right = BOOLEAN_LITERALS[right_token]
            return None, (operator, left, right)

    return "Invalid expression", None
