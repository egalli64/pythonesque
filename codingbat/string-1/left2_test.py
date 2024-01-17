"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

String 1: https://codingbat.com/python/String-1
left2: https://codingbat.com/prob/p160545
"""
import unittest
from left2 import left2


class TestNonStart(unittest.TestCase):
    def test_given_1(self):
        self.assertEqual(left2("Hello"), "lloHe")

    def test_given_2(self):
        self.assertEqual(left2("java"), "vaja")

    def test_given_3(self):
        self.assertEqual(left2("Hi"), "Hi")


if __name__ == "__main__":
    unittest.main()
