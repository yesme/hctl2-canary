import unittest

from clamp_abs import clamp_abs


class ClampAbsTests(unittest.TestCase):
    def test_below(self):
        for x, lo, hi in [(-10, -5, 5), (1, 2, 4), (-9, -8, -3)]:
            with self.subTest(x=x, lo=lo, hi=hi):
                self.assertEqual(clamp_abs(x, lo, hi), lo)

    def test_above(self):
        for x, lo, hi in [(10, -5, 5), (5, 2, 4), (-2, -8, -3)]:
            with self.subTest(x=x, lo=lo, hi=hi):
                self.assertEqual(clamp_abs(x, lo, hi), hi)

    def test_within(self):
        for x in [-5, -3, 0, 3, 5]:
            with self.subTest(x=x):
                self.assertEqual(clamp_abs(x, -5, 5), x)


if __name__ == "__main__":
    unittest.main()
