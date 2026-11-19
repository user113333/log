import unittest

from src.lexer import tokenize


class LexerTests(unittest.TestCase):
    def test_tokenizes_boolean_and_expression(self):
        self.assertEqual(
            tokenize("true and false"),
            (None, ["TRUE", "AND", "FALSE"]),
        )

    def test_reports_unknown_token(self):
        error, tokens = tokenize("true xor false")

        self.assertIsInstance(error, str)
        self.assertIn("xor", error)
        self.assertIsNone(tokens)
