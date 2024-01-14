"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

Warmup 1 https://codingbat.com/python/Warmup-1
makes10 https://codingbat.com/prob/p124984
"""


def makes10(a, b):
    """
    Parameters:
        a int
        b int
    return true if one of them is 10 or if their sum is 10
    """
    return a == 10 or b == 10 or a + b == 10
