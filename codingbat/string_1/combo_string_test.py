"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

String 1: https://codingbat.com/python/String-1
combo_string: https://codingbat.com/prob/p194053
"""
import unittest
from combo_string import combo_string


class TestComboString(unittest.TestCase):
    def test_given_1(self):
        self.assertEqual(combo_string("Hello", "hi"), "hiHellohi")

    def test_given_2(self):
        self.assertEqual(combo_string("hi", "Hello"), "hiHellohi")

    def test_given_3(self):
        self.assertEqual(combo_string("aaa", "b"), "baaab")


if __name__ == "__main__":
    unittest.main()
