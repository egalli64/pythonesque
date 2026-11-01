"""
LeetCode Easy Problems: https://leetcode.com/problemset/?difficulty=EASY
My solutions: https://github.com/egalli64/pythonesque/leetcode

1518. Water Bottles https://leetcode.com/problems/water-bottles/description/
"""
from ex_1518 import numWaterBottles


class TestWaterBottles:
    def test_given_1(self):
        assert numWaterBottles(9, 3) == 13

    def test_given_2(self):
        assert numWaterBottles(15, 4) == 19
