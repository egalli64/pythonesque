"""
LeetCode Problems: https://leetcode.com/problemset/
My solutions: https://github.com/egalli64/pythonesque/leetcode

217. Contains Duplicate https://leetcode.com/problems/contains-duplicate/
"""


def contains_duplicate(nums: list[int]) -> bool:
    """
    Return true there is at least a duplicate value, and return false if every element is distinct
    """
    return len(nums) > len(set(nums))


def contains_duplicate_alt(nums: list[int]) -> bool:
    """
    Return true there is at least a duplicate value, and return false if every element is distinct
    """
    buffer = set()

    for num in nums:
        if num in buffer:
            return True
        else:
            buffer.add(num)

    return False
