"""
LeetCode Medium Problems: https://leetcode.com/problemset/?difficulty=MEDIUM
My solutions: https://github.com/egalli64/pythonesque/leetcode

2962. Count Subarrays Where Max Element Appears at Least K Times
https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/description/
"""

from typing import List


def countSubarrays(nums: List[int], k: int) -> int:
    """
    Count how many subsequences in the passed list have the list maximum element repeated at least k times

    The list is non-empty
    """
    max_val = max(nums)
    result = 0

    left = 0
    count = 0
    for right_val in nums:
        if right_val == max_val:
            count += 1
        while count >= k:
            if nums[left] == max_val:
                count -= 1
            left += 1
        result += left

    return result
