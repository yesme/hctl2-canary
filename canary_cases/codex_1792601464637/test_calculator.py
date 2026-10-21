import unittest

from calculator import ceil_div


class CeilDivTests(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(ceil_div(7, 3), 3)

    def test_negative(self):
        for numerator, denominator, expected in [
            (-7, 3, -2),
            (7, -3, -2),
            (-7, -3, 3),
        ]:
            with self.subTest(numerator=numerator, denominator=denominator):
                self.assertEqual(ceil_div(numerator, denominator), expected)

    def test_exact(self):
        for numerator, denominator, expected in [
            (6, 3, 2), (-6, 3, -2), (6, -3, -2), (-6, -3, 2)
        ]:
            with self.subTest(numerator=numerator, denominator=denominator):
                self.assertEqual(ceil_div(numerator, denominator), expected)

    def test_zero_numerator(self):
        self.assertEqual(ceil_div(0, 3), 0)
        self.assertEqual(ceil_div(0, -3), 0)

    def test_zero_denominator(self):
        for numerator in (0, 7, -7):
            with self.subTest(numerator=numerator):
                with self.assertRaises(ValueError):
                    ceil_div(numerator, 0)

    def test_large_integers(self):
        self.assertEqual(ceil_div(10**100 + 1, 10), 10**99 + 1)


if __name__ == "__main__":
    unittest.main()
