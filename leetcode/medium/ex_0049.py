"""
LeetCode Problems: https://leetcode.com/problemset/
My solutions: https://github.com/egalli64/pythonesque/leetcode

49. Group Anagrams https://leetcode.com/problems/group-anagrams/description/
"""
from collections import defaultdict


def group_anagrams(strs: list[str]) -> list[list[str]]:
    """
    Group the anagrams together.
    """
    result: defaultdict[str, list[str]] = defaultdict(list)

    for s in strs:
        key = "".join(sorted(s))
        result[key].append(s)

    return list(result.values())


def group_anagrams_alt(strs: list[str]) -> list[list[str]]:
    result = {}

    for s in strs:
        key = tuple(sorted(s))
        result.setdefault(key, []).append(s)

    return list(result.values())
