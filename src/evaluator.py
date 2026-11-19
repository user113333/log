def evaluate(expression):
    match expression:
        case True: return None, True
        case False: return None, False
        case ("OR", left, right): return None, left or right
        case ("AND", left, right): return None, left and right
    return "No such expression"