if __package__:
    from .repl import loop
else:
    from repl import loop


if __name__ == "__main__":
    loop()
