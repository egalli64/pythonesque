"""
LeetCode Easy Problems: https://leetcode.com/problemset/?difficulty=EASY
My solutions: https://github.com/egalli64/pythonesque/leetcode

66. Plus One https://leetcode.com/problems/plus-one/
"""
from ex_0066 import plus_one


class TestPlusOne:
    def test_given_1(self):
        assert plus_one([1, 2, 3]) == [1, 2, 4]

    def test_given_2(self):
        assert plus_one([4, 3, 2, 1]) == [4, 3, 2, 2]

    def test_given_3(self):
        assert plus_one([9]) == [1, 0]
