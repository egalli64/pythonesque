"""
LeetCode Problems: https://leetcode.com/problemset/
My solutions: https://github.com/egalli64/pythonesque/leetcode

217. Contains Duplicate https://leetcode.com/problems/contains-duplicate/
"""
from ex_0217 import contains_duplicate


class TestSolution:
    def test_given_1(self):
        assert contains_duplicate([1, 2, 3, 1]) is True

    def test_given_2(self):
        assert contains_duplicate([1, 2, 3, 4]) is False

    def test_given_3(self):
        assert contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) is True
