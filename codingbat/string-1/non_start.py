"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

String 1: https://codingbat.com/python/String-1
non_start: https://codingbat.com/prob/p127703
"""


def non_start(a, b):
    """
    Parameters:
        a str non empty
        b str non empty
    return a without first char concatenated to b without first char
    """
    return a[1:] + b[1:]
