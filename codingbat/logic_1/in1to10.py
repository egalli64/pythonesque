"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

Logic 1: https://codingbat.com/python/Logic-1
in1to10: https://codingbat.com/prob/p158497
"""


def in1to10(n, outside_mode):
    """
    Parameters:
        n number
        outside_mode bool
    return True if n in [1..10]
        or, if outside_mode, is less or equal to 1 or greater or equal to 10
    """
    return n <= 1 or n >= 10 if outside_mode else 1 <= n <= 10
