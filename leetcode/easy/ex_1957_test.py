"""
LeetCode Easy Problems: https://leetcode.com/problemset/?difficulty=EASY
My solutions: https://github.com/egalli64/pythonesque/leetcode

1957. Delete Characters to Make Fancy String https://leetcode.com/problems/delete-characters-to-make-fancy-string/description/
"""
from ex_1957 import make_fancy_string


class TestMakeFancyString:
    def test_given_1(self):
        assert make_fancy_string("leeetcode") == "leetcode"

    def test_given_2(self):
        assert make_fancy_string("aaabaaaa") == "aabaa"

    def test_given_3(self):
        assert make_fancy_string("aab") == "aab"
