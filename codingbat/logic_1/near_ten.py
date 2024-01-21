"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

Logic 1: https://codingbat.com/python/Logic-1
near_ten: https://codingbat.com/prob/p165321
"""


def near_ten(num):
    """
    Parameters:
        num number
    return True if num is close to a multiple of 10, max distance is 2
    """
    reduced = num % 10
    return reduced <= 2 or reduced >= 8
