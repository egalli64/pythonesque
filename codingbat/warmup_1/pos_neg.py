"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

Warmup 1 https://codingbat.com/python/Warmup-1
pos_neg https://codingbat.com/prob/p162058
"""


def pos_neg(a, b, negative):
    """
    Parameters:
        a int
        b int
        negative boolean
    return true
        if a and b are one positive and the other negative
        but if negative is true only if both are negative
    """
    return a < 0 and b < 0 if negative else (a < 0) != (b < 0)
