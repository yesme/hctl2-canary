import unittest

from digit_sum import digit_sum


class DigitSumTests(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(digit_sum(0), 0)

    def test_positive(self):
        self.assertEqual(digit_sum(12345), 15)

    def test_negative(self):
        self.assertEqual(digit_sum(-907), 16)


if __name__ == "__main__":
    unittest.main()
