"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

Warmup 1 https://codingbat.com/python/Warmup-1
sum_double https://codingbat.com/prob/p141905
"""


def sum_double(a, b):
    """
    Parameters:
        a number
        b number
    return the a and b sum or, if the two values are the same, the doubled sum
    """
    return a + b if a != b else 4 * a
