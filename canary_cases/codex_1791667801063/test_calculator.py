import unittest

from calculator import ceil_div


class CeilDivTests(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(ceil_div(7, 3), 3)
        self.assertEqual(ceil_div(1, 3), 1)

    def test_negative_numerator(self):
        self.assertEqual(ceil_div(-7, 3), -2)
        self.assertEqual(ceil_div(-1, 3), 0)

    def test_negative_denominator(self):
        self.assertEqual(ceil_div(7, -3), -2)
        self.assertEqual(ceil_div(1, -3), 0)

    def test_both_negative(self):
        self.assertEqual(ceil_div(-7, -3), 3)

    def test_exact(self):
        for numerator, denominator, expected in (
            (6, 3, 2),
            (-6, 3, -2),
            (6, -3, -2),
            (-6, -3, 2),
        ):
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
        base = 10**100
        self.assertEqual(ceil_div(base + 1, 10), base // 10 + 1)
        self.assertEqual(ceil_div(-base - 1, 10), -base // 10)


if __name__ == "__main__":
    unittest.main()
