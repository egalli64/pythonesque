"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

List 1: https://codingbat.com/python/List-1
max_end3: https://codingbat.com/prob/p135290
"""


def max_end3(nums):
    """
    In-place

    Parameters:
        nums int list with length 3
    return nums, with all values set as the biggest value between its first and last value
    """
    value = max(nums[0], nums[-1])
    for i in range(len(nums)):
        nums[i] = value
    return nums


def max_end3_new(nums):
    """
    Returning another list

    Parameters:
        nums int list with length 3
    return nums, with all values set as the biggest value between its first and last value
    """
    return [max(nums[0], nums[-1])] * 3
