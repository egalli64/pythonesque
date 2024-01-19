"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

Logic 1: https://codingbat.com/python/Logic-1
sorta_sum: https://codingbat.com/prob/p116620
"""


def sorta_sum(a, b):
    """
    Parameters:
        a int
        b int
    return the parameters sum, but if it is in [10..19] set it to 20
    """
    sum = a + b
    return 20 if 10 <= sum <= 19 else sum
