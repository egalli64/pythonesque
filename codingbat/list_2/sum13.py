"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque codingbat folder

List 2: https://codingbat.com/python/List-2
sum13: https://codingbat.com/prob/p167025
"""


def sum13(nums: list[int]) -> int:
    """
    Parameters:
        nums a possibly empty int list
    return sum of values in nums, skipping 13 and elements following it
    """
    result = 0
    prev_13 = False

    for num in nums:
        if prev_13:
            prev_13 = False
        elif num == 13:
            prev_13 = True
        else:
            result += num

    return result
