"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

Warmup 1 https://codingbat.com/python/Warmup-1
front_back https://codingbat.com/prob/p153599
"""


def front_back(str):
    """
    Parameter:
        str a non-empty string
    return a copy of str with exchanged first and last char
    """
    return str if len(str) < 2 else str[-1] + str[1:-1] + str[0]
