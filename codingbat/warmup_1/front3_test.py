"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

Warmup 1 https://codingbat.com/python/Warmup-1
front3 https://codingbat.com/prob/p147920
"""
import unittest
from front3 import front3


class TestMissingChar(unittest.TestCase):
    def test_given_1(self):
        self.assertEqual(front3("Java"), "JavJavJav")

    def test_given_2(self):
        self.assertEqual(front3("Chocolate"), "ChoChoCho")

    def test_given_3(self):
        self.assertEqual(front3("abc"), "abcabcabc")

    def test_short(self):
        self.assertEqual(front3("a"), "aaa")


if __name__ == "__main__":
    unittest.main()
