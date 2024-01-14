"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

Warmup 2 https://codingbat.com/python/Warmup-2
front_times https://codingbat.com/prob/p165097
"""


def front_times(str, n):
    """
    Parameters:
        str
        n non-negative int
    Return a string built with n times the first three (or less) chars in str
    """
    return str[:3] * n
