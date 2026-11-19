def evaluate(expression):
    match expression:
        case True | False:
            return None, expression
        case ("OR", bool() as left, bool() as right):
            return None, left or right
        case ("AND", bool() as left, bool() as right):
            return None, left and right
    return "Invalid parsed expression", None
