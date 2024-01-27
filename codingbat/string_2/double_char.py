"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

String 2: https://codingbat.com/python/String-2
double_char: https://codingbat.com/prob/p170842
"""


def double_char(str):
    """
    Parameters:
        str
    return a duplicate of input, each char duplicated
    """
    return "".join(x * 2 for x in str)
