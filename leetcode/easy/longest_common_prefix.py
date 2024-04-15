"""
LeetCode Easy Problems: https://leetcode.com/problemset/?difficulty=EASY
My solutions: https://github.com/egalli64/pythonesque/leetcode

14. Longest Common Prefix: https://leetcode.com/problems/longest-common-prefix/description/
"""

from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
    """
    Get the longest common prefix string amongst the passed strings
    """
    strs = sorted(strs)

    result = ""
    for i in range(min(len(strs[0]),len(strs[-1]))):
        if strs[0][i] != strs[-1][i]:
            return result
        result += strs[0][i]
    return result
