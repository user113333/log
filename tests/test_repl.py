import subprocess
import sys
import unittest
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]


class ReplTests(unittest.TestCase):
    def test_continues_after_parse_error_and_exits_at_end_of_input(self):
        completed = subprocess.run(
            [sys.executable, "-B", "src/main.py"],
            cwd=PROJECT_ROOT,
            input="true false\ntrue and false\n",
            capture_output=True,
            text=True,
            timeout=5,
        )

        self.assertEqual(completed.returncode, 0, completed.stderr)
        self.assertEqual(completed.stderr, "")
        self.assertEqual(
            completed.stdout.splitlines(),
            ["Error: Parser: Invalid expression", "False"],
        )
