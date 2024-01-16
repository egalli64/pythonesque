"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

Warmup 2 https://codingbat.com/python/Warmup-2
array_count9 https://codingbat.com/prob/p166170
"""


def array_count9(nums):
    """
    Parameters:
        nums a list of ints
    Return how many 9s are in the array
    """
    return nums.count(9)


def array_count9_loop(nums):
    """
    Parameters:
        nums a list of ints
    Return how many 9s are in the array
    """
    count = 0
    for num in nums:
        if num == 9:
            count += 1
    return count
