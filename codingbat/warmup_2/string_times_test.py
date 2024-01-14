"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

Warmup 2 https://codingbat.com/python/Warmup-2
string_times https://codingbat.com/prob/p193507
"""
import unittest
from string_times import string_times


class TestStringTimes(unittest.TestCase):
    def test_given_1(self):
        self.assertEqual(string_times("Hi", 2), "HiHi")

    def test_given_2(self):
        self.assertEqual(string_times("Hi", 3), "HiHiHi")

    def test_given_3(self):
        self.assertEqual(string_times("Hi", 1), "Hi")


if __name__ == "__main__":
    unittest.main()
