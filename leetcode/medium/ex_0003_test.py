"""
LeetCode Problems: https://leetcode.com/problemset/
My solutions: https://github.com/egalli64/pythonesque/leetcode

3. Longest Substring Without Repeating Characters https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""
from ex_0003 import length_of_longest_substring,length_of_longest_substring_alt


class TestSolution:
    def test_given_1(self):
        assert length_of_longest_substring("abcabcbb") == 3

    def test_given_2(self):
        assert length_of_longest_substring("bbbbb") == 1

    def test_given_3(self):
        assert length_of_longest_substring("pwwkew") == 3

    def test_extra_1(self):
        assert length_of_longest_substring("1R1T7") == 4

    def test_extra_2(self):
        assert length_of_longest_substring("ccbbcc") == 2

class TestAltSolution:
    def test_given_1(self):
        assert length_of_longest_substring_alt("abcabcbb") == 3

    def test_given_2(self):
        assert length_of_longest_substring_alt("bbbbb") == 1

    def test_given_3(self):
        assert length_of_longest_substring_alt("pwwkew") == 3

    def test_extra_1(self):
        assert length_of_longest_substring_alt("1R1T7") == 4

    def test_extra_2(self):
        assert length_of_longest_substring_alt("ccbbcc") == 2
