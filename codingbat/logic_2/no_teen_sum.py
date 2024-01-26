"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

Logic 2: https://codingbat.com/python/Logic-2
no_teen_sum: https://codingbat.com/prob/p100347
"""


def no_teen_sum(a, b, c):
    """
    Parameters:
        a int
        b int
        c int
    Return the sum of parameters, "teen" excluded i.e. values in [13 .. 19], but 15 and 16 included
    """
    return fix_teen(a) + fix_teen(b) + fix_teen(c)


def fix_teen(n):
    """
    Parameters:
        n int
    Return value fixed following the "teen" rule
    """
    return 0 if (13 <= n <= 19) and n != 15 and n != 16 else n
