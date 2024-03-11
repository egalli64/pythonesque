"""
LeetCode Easy Problems: https://leetcode.com/problemset/?difficulty=EASY
My solutions: https://github.com/egalli64/pythonesque/leetcode

1. Two Sum: https://leetcode.com/problems/two-sum/description/
"""

from typing import List


class Solution:
    """
    Given an array and a target, return indices of the two elements that add up to target

    Each input would have exactly one solution, and you may not use the same element twice
    """

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        matchers = {}
        for i, num in enumerate(nums):
            matcher = target - num
            if matcher in matchers:
                return matchers[matcher], i
            else:
                matchers[num] = i
        return None
