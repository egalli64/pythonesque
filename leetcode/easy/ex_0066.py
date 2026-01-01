"""
LeetCode Easy Problems: https://leetcode.com/problemset/?difficulty=EASY
My solutions: https://github.com/egalli64/pythonesque/leetcode

66. Plus One
https://leetcode.com/problems/water-bottles/description/
"""

from typing import List


def plusOne(digits: List[int]) -> List[int]:
    """
    The input list represents an integer.
    Return a list representing the value increased by one
    """
    carry = 1

    for i, value in enumerate(reversed(digits)):
        if carry == 0:
            break

        total = value + carry
        digits[-(i + 1)] = total % 10
        carry = total // 10

    return digits if carry == 0 else [1] + digits
