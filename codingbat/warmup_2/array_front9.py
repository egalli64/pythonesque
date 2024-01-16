"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

Warmup 2 https://codingbat.com/python/Warmup-2
array_front9 https://codingbat.com/prob/p110166
"""


def array_front9(nums):
    """
    Parameters:
        nums a list of ints
    Return True if one of the first 4 elements (or less) is a 9
    """
    return nums[:4].count(9) > 0


def array_front9_no_slice(nums):
    """
    Parameters:
        nums a list of ints
    Return True if one of the first 4 elements (or less) is a 9
    """
    end = min(len(nums), 4)

    count = 0
    for i in range(end):
        if nums[i] == 9:
            count += 1

    return count > 0
