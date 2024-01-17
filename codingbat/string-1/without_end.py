"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

String 1: https://codingbat.com/python/String-1
without_end: https://codingbat.com/prob/p138533
"""


def without_end(str):
    """
    Parameters:
        str with length 2+
    return a copy of str without first and last char
    """
    return str[1:-1]
