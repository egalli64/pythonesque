"""
LeetCode Problems: https://leetcode.com/problemset/
My solutions: https://github.com/egalli64/pythonesque/leetcode

49. Group Anagrams https://leetcode.com/problems/group-anagrams/description/
"""
from ex_0049 import group_anagrams, group_anagrams_alt


class TestSolution:
    def test_given_1(self):
        actual = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
        expected = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
        assert {frozenset(item) for item in actual} == {frozenset(item) for item in expected}

    def test_given_2(self):
        assert group_anagrams([""]) == [[""]]

    def test_given_3(self):
        assert group_anagrams(["a"]) == [["a"]]

    def test_extra(self):
        actual = group_anagrams(["ddddddddddg", "dgggggggggg"])
        expected = [["dgggggggggg"], ["ddddddddddg"]]
        assert {frozenset(item) for item in actual} == {frozenset(item) for item in expected}


class TestSolutionAlt:
    def test_given_1(self):
        actual = group_anagrams_alt(["eat", "tea", "tan", "ate", "nat", "bat"])
        expected = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
        assert {frozenset(item) for item in actual} == {frozenset(item) for item in expected}

    def test_given_2(self):
        assert group_anagrams_alt([""]) == [[""]]

    def test_given_3(self):
        assert group_anagrams_alt(["a"]) == [["a"]]

    def test_extra(self):
        actual = group_anagrams_alt(["ddddddddddg", "dgggggggggg"])
        expected = [["dgggggggggg"], ["ddddddddddg"]]
        assert {frozenset(item) for item in actual} == {frozenset(item) for item in expected}
