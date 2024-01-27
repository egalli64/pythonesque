"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

String 2: https://codingbat.com/python/String-2
double_char: https://codingbat.com/prob/p170842
"""
import unittest
from double_char import double_char


class TestDoubleChar(unittest.TestCase):
    def test_given_1(self):
        self.assertEqual(double_char("The"), "TThhee")

    def test_given_2(self):
        self.assertEqual(double_char("AAbb"), "AAAAbbbb")

    def test_given_3(self):
        self.assertEqual(double_char("Hi-There"), "HHii--TThheerree")


if __name__ == "__main__":
    unittest.main()
