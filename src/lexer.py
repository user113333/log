TOKENS = {
    "true": "TRUE",
    "false": "FALSE",
    "and": "AND",
    "or": "OR"
}

def tokenize(s):
    tokens = []
    for w in s.split():
        if w not in TOKENS:
            return f"({w} token does not exist", None
        tokens.append(TOKENS[w])
    return None, tokens