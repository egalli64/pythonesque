"""
LeetCode Easy Problems: https://leetcode.com/problemset/?difficulty=EASY
My solutions: https://github.com/egalli64/pythonesque/leetcode

13. Roman to Integer: https://leetcode.com/problems/roman-to-integer/description/
"""
from ex_0013 import roman_to_int


class TestRomanToInt:
    def test_given_1(self):
        assert roman_to_int("III") == 3

    def test_given_2(self):
        assert roman_to_int("LVIII") == 58

    def test_given_3(self):
        assert roman_to_int("MCMXCIV") == 1994
