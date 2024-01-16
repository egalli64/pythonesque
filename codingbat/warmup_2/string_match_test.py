"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

Warmup 2 https://codingbat.com/python/Warmup-2
string_match https://codingbat.com/prob/p182414
"""
import unittest
from string_match import string_match


class TestStringMatch(unittest.TestCase):
    def test_given_1(self):
        self.assertEqual(string_match("xxcaazz", "xxbaaz"), 3)

    def test_given_2(self):
        self.assertEqual(string_match("abc", "abc"), 2)

    def test_given_3(self):
        self.assertEqual(string_match("abc", "axc"), 0)


if __name__ == "__main__":
    unittest.main()
