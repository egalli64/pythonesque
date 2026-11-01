"""
LeetCode Easy Problems: https://leetcode.com/problemset/?difficulty=EASY
My solutions: https://github.com/egalli64/pythonesque/leetcode

1550. Three Consecutive Odds: https://leetcode.com/problems/three-consecutive-odds/description/
"""
from ex_1550 import three_consecutive_odds, three_consecutive_odds_for_else


class TestThreeConsecutiveOdds:
    def test_given_1(self):
        assert three_consecutive_odds([2, 6, 4, 1]) is False

    def test_given_2(self):
        assert three_consecutive_odds([1, 2, 34, 3, 4, 5, 7, 23, 12]) is True


class TestThreeConsecutiveOddsForElse:
    def test_given_1(self):
        assert three_consecutive_odds_for_else([2, 6, 4, 1]) is False

    def test_given_2(self):
        assert three_consecutive_odds_for_else([1, 2, 34, 3, 4, 5, 7, 23, 12]) is True
