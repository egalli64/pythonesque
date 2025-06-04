"""
LeetCode Medium Problems: https://leetcode.com/problemset/?difficulty=MEDIUM
My solutions: https://github.com/egalli64/pythonesque/leetcode

3403. Find the Lexicographically Largest String From the Box I
https://leetcode.com/problems/find-the-lexicographically-largest-string-from-the-box-i/description/
"""

import unittest
from ex_3403 import answerString


class TestTwoSum(unittest.TestCase):
    def test_given_1(self):
        self.assertEqual(answerString("dbca", 2), "dbc")

    def test_given_2(self):
        self.assertEqual(answerString("gggg", 4), "g")

    def test_single_friend(self):
        self.assertEqual(answerString("gh", 1), "gh")


if __name__ == "__main__":
    unittest.main()
