"""
LeetCode Easy Problems: https://leetcode.com/problemset/?difficulty=EASY
My solutions: https://github.com/egalli64/pythonesque/leetcode

1957. Delete Characters to Make Fancy String
https://leetcode.com/problems/delete-characters-to-make-fancy-string/description/
"""

import unittest
from ex_1957 import makeFancyString


class TestTwoSum(unittest.TestCase):
    def test_given_1(self):
        self.assertEqual(makeFancyString("leeetcode"), "leetcode")

    def test_given_2(self):
        self.assertEqual(makeFancyString("aaabaaaa"), "aabaa")

    def test_given_3(self):
        self.assertEqual(makeFancyString("aab"), "aab")


if __name__ == "__main__":
    unittest.main()
