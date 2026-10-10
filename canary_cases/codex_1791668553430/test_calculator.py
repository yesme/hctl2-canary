"""Tests for signed integer ceiling division."""

import unittest

from calculator import ceil_div


class CeilDivTests(unittest.TestCase):
    def test_positive_inputs(self):
        for numerator, denominator, expected in [(7, 3, 3), (1, 3, 1)]:
            with self.subTest(numerator=numerator, denominator=denominator):
                self.assertEqual(ceil_div(numerator, denominator), expected)

    def test_negative_inputs(self):
        cases = [(-7, 3, -2), (7, -3, -2), (-7, -3, 3), (-1, 3, 0), (1, -3, 0)]
        for numerator, denominator, expected in cases:
            with self.subTest(numerator=numerator, denominator=denominator):
                self.assertEqual(ceil_div(numerator, denominator), expected)

    def test_exact_division(self):
        cases = [(6, 3, 2), (-6, 3, -2), (6, -3, -2), (-6, -3, 2)]
        for numerator, denominator, expected in cases:
            with self.subTest(numerator=numerator, denominator=denominator):
                self.assertEqual(ceil_div(numerator, denominator), expected)

    def test_zero_numerator(self):
        for denominator in (3, -3):
            with self.subTest(denominator=denominator):
                self.assertEqual(ceil_div(0, denominator), 0)

    def test_zero_denominator(self):
        for numerator in (0, 1, -1):
            with self.subTest(numerator=numerator):
                with self.assertRaises(ValueError):
                    ceil_div(numerator, 0)

    def test_large_integers(self):
        large = 10**100
        cases = [
            (large + 1, large, 2),
            (-(large + 1), large, -1),
            (large + 1, -large, -1),
            (-(large + 1), -large, 2),
        ]
        for numerator, denominator, expected in cases:
            with self.subTest(numerator=numerator, denominator=denominator):
                self.assertEqual(ceil_div(numerator, denominator), expected)


if __name__ == "__main__":
    unittest.main()
