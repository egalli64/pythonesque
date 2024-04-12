"""
LeetCode Easy Problems: https://leetcode.com/problemset/?difficulty=EASY
My solutions: https://github.com/egalli64/pythonesque/leetcode

13. Roman to Integer: https://leetcode.com/problems/roman-to-integer/description/
"""

MAPPER = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


def romanToInt(s: str) -> int:
    """
    Convert a Roman number to its integer representation
    """
    result = 0

    prev = 0
    for c in reversed(s):
        cur = MAPPER[c]
        if cur < prev:
            result -= cur
        else:
            result += cur
        prev = cur

    return result
