"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque codingbat folder

List 2: https://codingbat.com/python/List-2
has22: https://codingbat.com/prob/p119308
"""
from itertools import pairwise


def has22_modern(nums: list[int]) -> bool:
    """
    Parameters:
        nums a possibly empty int list
    return True if nums has two adjacent twos
    """
    for left, right in pairwise(nums):
        if left == 2 and right == 2:
            return True
    return False


def has22_zip(nums: list[int]) -> bool:
    """
    Parameters:
        nums a possibly empty int list
    return True if nums has two adjacent twos
    """
    for left, right in zip(nums, nums[1:]):
        if left == 2 and right == 2:
            return True
    return False


def has22(nums: list[int]) -> bool:
    """
    Parameters:
        nums a possibly empty int list
    return True if nums has two adjacent twos
    """
    for i in range(len(nums) - 1):
        if nums[i] == 2 and nums[i + 1] == 2:
            return True
    return False
