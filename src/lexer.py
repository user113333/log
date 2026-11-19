KEYWORD_TOKENS = {
    "true": "TRUE",
    "false": "FALSE",
    "and": "AND",
    "or": "OR",
}


def tokenize(source):
    tokens = []
    for word in source.split():
        token = KEYWORD_TOKENS.get(word)
        if token is None:
            return f"Unknown keyword {word!r}", None
        tokens.append(token)
    return None, tokens
