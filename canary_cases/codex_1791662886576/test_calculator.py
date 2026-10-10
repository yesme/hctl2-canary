import unittest

from calculator import ceil_div


class CeilDivTests(unittest.TestCase):
    def test_positive(self):
        for numerator, denominator, expected in [(7, 3, 3), (1, 2, 1)]:
            with self.subTest(numerator=numerator, denominator=denominator):
                self.assertEqual(ceil_div(numerator, denominator), expected)

    def test_negative(self):
        cases = [(-7, 3, -2), (7, -3, -2), (-7, -3, 3), (-1, 2, 0), (1, -2, 0)]
        for numerator, denominator, expected in cases:
            with self.subTest(numerator=numerator, denominator=denominator):
                self.assertEqual(ceil_div(numerator, denominator), expected)

    def test_exact(self):
        cases = [(6, 3, 2), (-6, 3, -2), (6, -3, -2), (-6, -3, 2)]
        for numerator, denominator, expected in cases:
            with self.subTest(numerator=numerator, denominator=denominator):
                self.assertEqual(ceil_div(numerator, denominator), expected)

    def test_zero_numerator(self):
        for denominator in (3, -3):
            with self.subTest(denominator=denominator):
                self.assertEqual(ceil_div(0, denominator), 0)

    def test_zero_denominator(self):
        for numerator in (7, -7, 0):
            with self.subTest(numerator=numerator):
                with self.assertRaises(ValueError):
                    ceil_div(numerator, 0)

    def test_large_integers(self):
        numerator = 2**100 + 1
        self.assertEqual(ceil_div(numerator, 2), 2**99 + 1)
        self.assertEqual(ceil_div(-numerator, 2), -(2**99))
        self.assertEqual(ceil_div(numerator, -2), -(2**99))
        self.assertEqual(ceil_div(-numerator, -2), 2**99 + 1)


if __name__ == "__main__":
    unittest.main()
