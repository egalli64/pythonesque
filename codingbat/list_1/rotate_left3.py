"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

List 1: https://codingbat.com/python/List-1
rotate_left3: https://codingbat.com/prob/p148661
"""


def rotate_left3(nums):
    """
    Parameters:
        nums int list with length 3
    return the left rotation-1 of nums
    """
    return nums[1:] + nums[:1]
