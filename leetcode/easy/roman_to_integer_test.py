"""
LeetCode Easy Problems: https://leetcode.com/problemset/?difficulty=EASY
My solutions: https://github.com/egalli64/pythonesque/leetcode

13. Roman to Integer: https://leetcode.com/problems/roman-to-integer/description/
"""

import unittest
from roman_to_integer import romanToInt


class TestRomanToInt(unittest.TestCase):
    def test_given_1(self):
        self.assertEqual(romanToInt("III"), 3)

    def test_given_2(self):
        self.assertEqual(romanToInt("LVIII"), 58)

    def test_given_3(self):
        self.assertEqual(romanToInt("MCMXCIV"), 1994)


if __name__ == "__main__":
    unittest.main()
