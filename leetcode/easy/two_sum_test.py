"""
LeetCode Easy Problems: https://leetcode.com/problemset/?difficulty=EASY
My solutions: https://github.com/egalli64/pythonesque/leetcode

1. Two Sum: https://leetcode.com/problems/two-sum/description/
"""

import unittest
from two_sum import twoSum


class TestSum3(unittest.TestCase):
    def test_given_1(self):
        self.assertCountEqual(twoSum([2, 7, 11, 15], 9), [0, 1])

    def test_given_2(self):
        self.assertCountEqual(twoSum([3, 2, 4], 6), [1, 2])

    def test_given_3(self):
        self.assertCountEqual(twoSum([3, 3], 6), [0, 1])


if __name__ == "__main__":
    unittest.main()
