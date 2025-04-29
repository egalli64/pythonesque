"""
LeetCode Medium Problems: https://leetcode.com/problemset/?difficulty=MEDIUM
My solutions: https://github.com/egalli64/pythonesque/leetcode

2962. Count Subarrays Where Max Element Appears at Least K Times
https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/description/
"""

import unittest
from ex_2962 import countSubarrays


class TestTwoSum(unittest.TestCase):
    def test_given_1(self):
        self.assertEqual(countSubarrays([1, 3, 2, 3, 3], 2), 6)

    def test_given_2(self):
        self.assertEqual(countSubarrays([1, 4, 2, 1], 3), 0)


if __name__ == "__main__":
    unittest.main()
