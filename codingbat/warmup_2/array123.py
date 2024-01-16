"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

Warmup 2 https://codingbat.com/python/Warmup-2
array123 https://codingbat.com/prob/p193604
"""


def array123(nums):
    """
    Parameters:
        nums a list of ints
    Return True if nums contains the subsequence 1, 2, 3
    """
    for i in range(len(nums) - 2):
        if nums[i : i + 3] == [1, 2, 3]:
            return True
    return False


def array123_any(nums):
    """
    Parameters:
        nums a list of ints
    Return True if nums contains the subsequence 1, 2, 3
    """
    return any(nums[i : i + 3] == [1, 2, 3] for i in range(len(nums) - 2))
