import unittest

from sign_abs import sign_abs


class SignAbsTests(unittest.TestCase):
    def test_positive(self):
        for value in (1, 7, 10**100):
            with self.subTest(value=value):
                self.assertEqual(sign_abs(value), value)

    def test_negative(self):
        for value in (-1, -7, -(10**100)):
            with self.subTest(value=value):
                self.assertEqual(sign_abs(value), value)

    def test_zero(self):
        self.assertEqual(sign_abs(0), 0)


if __name__ == "__main__":
    unittest.main()
