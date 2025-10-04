"""
LeetCode Medium Problems: https://leetcode.com/problemset/?difficulty=MEDIUM
My solutions: https://github.com/egalli64/pythonesque/leetcode

2962. Count Subarrays Where Max Element Appears at Least K Times
https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/description/
"""

import unittest
from ex_0011 import maxArea


class TestMaxArea(unittest.TestCase):
    def test_given_1(self):
        self.assertEqual(maxArea([1,8,6,2,5,4,8,3,7]), 49)

    def test_given_2(self):
        self.assertEqual(maxArea([1, 1]), 1)


if __name__ == "__main__":
    unittest.main()
