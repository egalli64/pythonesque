"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

String 1: https://codingbat.com/python/String-1
combo_string: https://codingbat.com/prob/p194053
"""


def combo_string(a, b):
    """
    Parameters:
        a str
        b str
    return a concatenation of a and b, where the longest one is between two copies of the shorter one
    """
    longer = a if len(a) > len(b) else b
    shorter = b if len(b) < len(a) else a
    return shorter + longer + shorter
