"""
LeetCode Easy Problems: https://leetcode.com/problemset/?difficulty=EASY
My solutions: https://github.com/egalli64/pythonesque/leetcode

9. Palindrome Number: https://leetcode.com/problems/palindrome-number/description/
"""
from ex_0009 import is_palindrome


class TestIsPalindrome:
    def test_given_1(self):
        assert is_palindrome(121) is True

    def test_given_2(self):
        assert is_palindrome(-121) is False

    def test_given_3(self):
        assert is_palindrome(10) is False
