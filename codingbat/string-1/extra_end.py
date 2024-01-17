"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

String 1: https://codingbat.com/python/String-1
extra_end: https://codingbat.com/prob/p148853
"""


def extra_end(str):
    """
    Parameters:
        str lenght 2+
    return the concatenation of three times the last 2 char in str
    """
    return str[-2:] * 3
