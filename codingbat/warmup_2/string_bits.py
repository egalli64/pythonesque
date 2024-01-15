"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

Warmup 2 https://codingbat.com/python/Warmup-2
string_bits https://codingbat.com/prob/p113152
"""


def string_bits(str):
    """
    Parameters:
        str
    Return a copy of str, discarding any other chars (keep the first, discard the second, ...)
    """
    return str[::2]
