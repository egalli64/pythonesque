"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

Warmup 2 https://codingbat.com/python/Warmup-2
string_splosion https://codingbat.com/prob/p118366
"""
import unittest
from string_splosion import string_splosion


class TestStringBits(unittest.TestCase):
    def test_given_1(self):
        self.assertEqual(string_splosion("Code"), "CCoCodCode")

    def test_given_2(self):
        self.assertEqual(string_splosion("abc"), "aababc")

    def test_given_3(self):
        self.assertEqual(string_splosion("ab"), "aab")


if __name__ == "__main__":
    unittest.main()
