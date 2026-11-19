import unittest

from src.parser import parse


class ParserTests(unittest.TestCase):
    def test_rejects_two_literals_without_an_operator(self):
        error, expression = parse(["TRUE", "FALSE"])

        self.assertTrue(error)
        self.assertIsNone(expression)
