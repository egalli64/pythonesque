"""
LeetCode Easy Problems: https://leetcode.com/problemset/?difficulty=EASY
My solutions: https://github.com/egalli64/pythonesque/leetcode

387. First Unique Character in a String https://leetcode.com/problems/first-unique-character-in-a-string/
"""
from collections import Counter


def first_uniq_char(s: str) -> int:
    """
    Find the first non-repeating character in the input string and return its index.

    If it does not exist, return -1.
    """
    counter = Counter(s)

    for i, ch in enumerate(s):
        if counter[ch] == 1:
            return i

    return -1
