"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

List 1: https://codingbat.com/python/List-1
first_last6: https://codingbat.com/prob/p181624
"""


def first_last6(nums):
    """
    Parameters:
        nums int list with length 1+
    return True is 6 in first or last position
    """
    return nums[0] == 6 or nums[-1] == 6
