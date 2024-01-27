"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

Logic 2: https://codingbat.com/python/Logic-2
close_far: https://codingbat.com/prob/p160533
"""


def close_far(a, b, c):
    """
    Parameters:
        a int
        b int
        c int
    Return True if b or c is close to a, and the other is 2+ away to the other two
    """
    return close(b, a) and far(c, a, b) or close(c, a) and far(b, a, c)


def close(x, target):
    return abs(x - target) <= 1


def far(x, t1, t2):
    return abs(x - t1) >= 2 and abs(x - t2) >= 2
