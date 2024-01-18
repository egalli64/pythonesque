"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

List 1: https://codingbat.com/python/List-1
same_first_last: https://codingbat.com/prob/p179078
"""


def same_first_last(nums):
    """
    Parameters:
        nums int list
    return True if nums is non-empty and first elements equals last elements
    """
    return bool(len(nums)) and nums[0] == nums[-1]
