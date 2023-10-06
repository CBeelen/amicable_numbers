import unittest

from src.amicable_numbers import get_divisors, are_amicable


class DivisorTests(unittest.TestCase):
    def test_divisors(self):
        n = 50
        expected_divisors = [1, 2, 5, 10, 25]

        self.assertListEqual(get_divisors(n), expected_divisors)


class AmicableTests(unittest.TestCase):
    def test_amicable(self):
        n = 220
        m = 284

        self.assertEquals(are_amicable(n, m), True)

    def test_not_amicable(self):
        n = 3
        m = 4

        self.assertEquals(are_amicable(n, m), False)
        