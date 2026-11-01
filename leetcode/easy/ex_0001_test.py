"""
LeetCode Easy Problems: https://leetcode.com/problemset/?difficulty=EASY
My solutions: https://github.com/egalli64/pythonesque/leetcode

1. Two Sum: https://leetcode.com/problems/two-sum/description/
"""
import pytest

from ex_0001 import two_sum


class TestTwoSum:
    def test_given_1(self):
        assert two_sum([2, 7, 11, 15], 9) == [0, 1]

    def test_given_2(self):
        assert two_sum([3, 2, 4], 6) == [1, 2]

    def test_given_3(self):
        assert two_sum([3, 3], 6) == [0, 1]

    def test_empty(self):
        with pytest.raises(ValueError):
            two_sum([], 42)

    def test_bad_input(self):
        with pytest.raises(ValueError):
            two_sum([4, 2], 42)
