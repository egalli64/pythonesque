"""
LeetCode: https://leetcode.com/problemset/
My solutions: https://github.com/egalli64/pythonesque/leetcode

20. Valid Parentheses
"""
from ex_0020 import is_valid


class TestSolution:
    def test_given_1(self):
        assert is_valid("()") is True

    def test_given_2(self):
        assert is_valid("()[]{}") is True

    def test_given_3(self):
        assert is_valid("(]") is False

    def test_given_4(self):
        assert is_valid("([])") is True

    def test_given_5(self):
        assert is_valid("([)]") is False
