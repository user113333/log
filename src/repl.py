if __package__:
    from .evaluator import evaluate
    from .lexer import tokenize
    from .parser import parse
else:
    from evaluator import evaluate
    from lexer import tokenize
    from parser import parse


def evaluate_prompt(source):
    err, tokens = tokenize(source)
    if err is not None:
        return "Lexer: " + err, None
    err, expression = parse(tokens)
    if err is not None:
        return "Parser: " + err, None
    err, result = evaluate(expression)
    if err is not None:
        return "Evaluator: " + err, None
    return None, result


def loop():
    while True:
        try:
            source = input()
        except EOFError:
            return
        if source.strip() == "exit":
            return
        err, result = evaluate_prompt(source)
        if err is None:
            print(result)
        else:
            print("Error: " + err)
