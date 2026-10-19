"""Tests for text wrapping."""

import unittest

from wrap_text import wrap_text


class TestWrapText(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(wrap_text("hello world from Python", 11),
                         "hello world\nfrom Python")

    def test_empty(self):
        self.assertEqual(wrap_text("", 10), "")

    def test_narrow(self):
        self.assertEqual(wrap_text("abc de", 1), "a\nb\nc\nd\ne")


if __name__ == "__main__":
    unittest.main()
