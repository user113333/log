import unittest

from src.evaluator import evaluate


class EvaluatorTests(unittest.TestCase):
    def test_evaluates_standalone_false(self):
        error, result = evaluate(False)

        self.assertIsNone(error)
        self.assertIs(result, False)

    def test_evaluates_or_with_one_true_operand(self):
        error, result = evaluate(("OR", False, True))

        self.assertIsNone(error)
        self.assertIs(result, True)

    def test_rejects_non_boolean_operand(self):
        error, result = evaluate(("AND", True, "FALSE"))

        self.assertTrue(error)
        self.assertIsNone(result)
