import unittest

from src.amicable_numbers import get_divisors


class DivisorTests(unittest.TestCase):
    def test_divisors(self):
        n = 50
        expected_divisors = [1, 2, 5, 10, 25]

        self.assertListEqual(get_divisors(n), expected_divisors)
