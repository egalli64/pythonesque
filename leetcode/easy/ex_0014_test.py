"""
LeetCode Easy Problems: https://leetcode.com/problemset/?difficulty=EASY
My solutions: https://github.com/egalli64/pythonesque/leetcode

14. Longest Common Prefix: https://leetcode.com/problems/longest-common-prefix/description/
"""
from ex_0014 import longest_common_prefix


class TestLongestCommonPrefix:
    def test_given_1(self):
        assert longest_common_prefix(["flower", "flow", "flight"]) == "fl"

    def test_given_2(self):
        assert longest_common_prefix(["dog", "racecar", "car"]) == ""
