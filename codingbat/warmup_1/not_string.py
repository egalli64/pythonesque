"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

Warmup 1 https://codingbat.com/python/Warmup-1
not_string https://codingbat.com/prob/p189441
"""


def not_string(str):
    """
    Parameter:
        str
    return str prefixed with "not " but only if it does not start with "not"
    """
    return str if str.startswith("not") else "not " + str
