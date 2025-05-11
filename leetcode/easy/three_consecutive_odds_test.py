"""
LeetCode Easy Problems: https://leetcode.com/problemset/?difficulty=EASY
My solutions: https://github.com/egalli64/pythonesque/leetcode

1550. Three Consecutive Odds: https://leetcode.com/problems/three-consecutive-odds/description/
"""

import unittest
from three_consecutive_odds import threeConsecutiveOdds


class TestPalindromeNumber(unittest.TestCase):
    def test_given_1(self):
        self.assertFalse(threeConsecutiveOdds([2, 6, 4, 1]))

    def test_given_2(self):
        self.assertTrue(threeConsecutiveOdds([1, 2, 34, 3, 4, 5, 7, 23, 12]))


if __name__ == "__main__":
    unittest.main()
