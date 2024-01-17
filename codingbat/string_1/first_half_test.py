"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

String 1: https://codingbat.com/python/String-1
first_half: https://codingbat.com/prob/p107010
"""
import unittest
from first_half import first_half


class TestFirstHalf(unittest.TestCase):
    def test_given_1(self):
        self.assertEqual(first_half("WooHoo"), "Woo")

    def test_given_2(self):
        self.assertEqual(first_half("HelloThere"), "Hello")

    def test_given_3(self):
        self.assertEqual(first_half("abcdef"), "abc")


if __name__ == "__main__":
    unittest.main()
