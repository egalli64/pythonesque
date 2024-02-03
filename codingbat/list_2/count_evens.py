"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

List 2: https://codingbat.com/python/List-2
count_evens: https://codingbat.com/prob/p189616
"""


def count_evens(nums: list):
    """
    Parameters:
        nums int list
    return the number of even values in nums
    """
    return sum(num % 2 == 0 for num in nums)
