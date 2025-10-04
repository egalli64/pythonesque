"""
LeetCode Medium Problems: https://leetcode.com/problemset/?difficulty=MEDIUM
My solutions: https://github.com/egalli64/pythonesque/leetcode

11. Container With Most Water
https://leetcode.com/problems/container-with-most-water/description/
"""

from typing import List


def maxArea(height: List[int]) -> int:
    """
    Find the largest rectangle having vertical sizes in the input list
    """
    left = 0
    right = len(height) - 1
    result = 0

    while left < right:
        result = max(result, min(height[left], height[right]) * (right - left))
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return result
