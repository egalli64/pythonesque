"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

Warmup 1 https://codingbat.com/python/Warmup-1
diff21 https://codingbat.com/prob/p197466
"""


def diff21(n):
    """
    Parameter:
        n int
    return the absolute difference between n and 21, but double it if it is over 21
    """
    return abs(n - 21) * ((n > 21) + 1)

def diff21_more_readable(n):
    """
    Parameter:
        n int
    return the absolute difference between n and 21, but double it if it is over 21
    """
    diff = abs(n - 21)
    return 2 * diff if n > 21 else diff
