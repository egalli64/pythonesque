"""
LeetCode Easy Problems: https://leetcode.com/problemset/?difficulty=EASY
My solutions: https://github.com/egalli64/pythonesque/leetcode

14. Longest Common Prefix: https://leetcode.com/problems/longest-common-prefix/description/
"""

import unittest
from longest_common_prefix import longestCommonPrefix


class TestPalindromeNumber(unittest.TestCase):
    def test_given_1(self):
        self.assertEqual(longestCommonPrefix(["flower","flow","flight"]), "fl")

    def test_given_2(self):
        self.assertFalse(longestCommonPrefix(["dog","racecar","car"]), "")


if __name__ == "__main__":
    unittest.main()
