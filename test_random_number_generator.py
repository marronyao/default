import io
import unittest
from contextlib import redirect_stderr, redirect_stdout
from unittest.mock import patch

from random_number_generator import main, random_integer


class RandomIntegerTests(unittest.TestCase):
    def test_returns_value_in_inclusive_range(self):
        with patch("random_number_generator.secrets.randbelow", return_value=4) as randbelow:
            self.assertEqual(random_integer(-2, 2), 2)
        randbelow.assert_called_once_with(5)

    def test_rejects_reversed_range(self):
        with self.assertRaisesRegex(ValueError, "minimum must be less"):
            random_integer(9, 3)

    def test_cli_prints_requested_number_of_values(self):
        output = io.StringIO()
        with patch("random_number_generator.secrets.randbelow", side_effect=[0, 2, 1]):
            with redirect_stdout(output):
                exit_code = main(["10", "12", "--count", "3"])

        self.assertEqual(exit_code, 0)
        self.assertEqual(output.getvalue(), "10\n12\n11\n")

    def test_cli_rejects_invalid_count(self):
        output = io.StringIO()
        with redirect_stderr(output):
            exit_code = main(["1", "2", "--count", "0"])

        self.assertEqual(exit_code, 2)
        self.assertEqual(output.getvalue(), "error: count must be at least 1\n")


if __name__ == "__main__":
    unittest.main()
