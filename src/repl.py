from lexer import tokenize
from parser import parse
from evaluator import evaluate

def evaluate_prompt(p):
    err, tokens = tokenize(p)
    if err is not None:
        return "Lexer: " + err, None
    err, expression = parse(tokens)
    if err is not None:
        return "Parser: " + err, None
    err, res = evaluate(expression)
    if err is not None:
        return "Evaluator: " + err, None
    return None, res

def loop():
    while True:
        prompt = input()
        if prompt == "exit":
            break
        err, res = evaluate_prompt(prompt)
        if err is None:
            print(res)
        else:
            print("Error: " + err)
