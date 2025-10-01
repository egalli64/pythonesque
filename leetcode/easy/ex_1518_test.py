"""
LeetCode Easy Problems: https://leetcode.com/problemset/?difficulty=EASY
My solutions: https://github.com/egalli64/pythonesque/leetcode

1518. Water Bottles
https://leetcode.com/problems/water-bottles/description/
"""

import unittest
from ex_1518 import numWaterBottles


class TestTwoSum(unittest.TestCase):
    def test_given_1(self):
        self.assertEqual(numWaterBottles(9,3), 13)

    def test_given_2(self):
        self.assertEqual(numWaterBottles(15,4), 19)

if __name__ == "__main__":
    unittest.main()
