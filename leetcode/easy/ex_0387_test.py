"""
LeetCode Easy Problems: https://leetcode.com/problemset/?difficulty=EASY
My solutions: https://github.com/egalli64/pythonesque/leetcode

387. First Unique Character in a String https://leetcode.com/problems/first-unique-character-in-a-string/
"""
from ex_0387 import first_uniq_char


class TestSolution:
    def test_given_1(self):
        assert first_uniq_char("leetcode") == 0

    def test_given_2(self):
        assert first_uniq_char("loveleetcode") == 2

    def test_given_3(self):
        assert first_uniq_char("aabb") == -1
