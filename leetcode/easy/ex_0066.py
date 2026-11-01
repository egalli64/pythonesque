"""
LeetCode Easy Problems: https://leetcode.com/problemset/?difficulty=EASY
My solutions: https://github.com/egalli64/pythonesque/leetcode

66. Plus One https://leetcode.com/problems/plus-one/
"""


def plus_one(digits: list[int]) -> list[int]:
    """Given an integer represented as list of digits, increase the integer representation, and return it."""
    carry = 1

    for i, value in enumerate(reversed(digits)):
        if carry == 0:
            break

        total = value + carry
        digits[-(i + 1)] = total % 10
        carry = total // 10

    return digits if carry == 0 else [1] + digits
