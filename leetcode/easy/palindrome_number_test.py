"""
LeetCode Easy Problems: https://leetcode.com/problemset/?difficulty=EASY
My solutions: https://github.com/egalli64/pythonesque/leetcode

9. Palindrome Number: https://leetcode.com/problems/palindrome-number/description/
"""

import unittest
from palindrome_number import isPalindrome


class TestPalindromeNumber(unittest.TestCase):
    def test_given_1(self):
        self.assertTrue(isPalindrome(121))

    def test_given_2(self):
        self.assertFalse(isPalindrome(-121))

    def test_given_3(self):
        self.assertFalse(isPalindrome(10))


if __name__ == "__main__":
    unittest.main()
