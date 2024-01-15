"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

Warmup 2 https://codingbat.com/python/Warmup-2
string_bits https://codingbat.com/prob/p113152
"""
import unittest
from string_bits import string_bits


class TestStringBits(unittest.TestCase):
    def test_given_1(self):
        self.assertEqual(string_bits("Hello"), "Hlo")

    def test_given_2(self):
        self.assertEqual(string_bits("Hi"), "H")

    def test_given_3(self):
        self.assertEqual(string_bits("Heeololeo"), "Hello")


if __name__ == "__main__":
    unittest.main()
