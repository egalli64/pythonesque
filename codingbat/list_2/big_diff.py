"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque codingbat folder

List 2: https://codingbat.com/python/List-2
big_diff: https://codingbat.com/prob/p184853
"""


def big_diff(nums: list[int]) -> int:
    """
    Parameters:
        nums a non-empty int list
    return the difference between the largest and smallest numbers in the input list
    """
    return max(nums) - min(nums)
