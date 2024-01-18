"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

List 1: https://codingbat.com/python/List-1
common_end: https://codingbat.com/prob/p147755
"""


def common_end(a, b):
    """
    Parameters:
        a int list with length 1+
        b int list with length 1+
    return True if both a and b have the same first or last element
    """
    return a[0] == b[0] or a[-1] == b[-1]
