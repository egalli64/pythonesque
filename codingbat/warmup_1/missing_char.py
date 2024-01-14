"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

Warmup 1 https://codingbat.com/python/Warmup-1
missing_char https://codingbat.com/prob/p149524
"""


def missing_char(str, n):
    """
    Parameter:
        str a non-empty string
        n an int in [0 .. len(str))
    return a copy of str without the n-th char
    """
    return str[:n] + str[n + 1 :]
