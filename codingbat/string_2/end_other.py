"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

String 2: https://codingbat.com/python/String-2
end_other: https://codingbat.com/prob/p174314
"""


def end_other(a: str, b: str):
    """
    Parameters:
        a str
        b str
    Return True if one str is at the end of the other - case insensitive
    """
    a = a.lower()
    b = b.lower()

    return a.endswith(b) or b.endswith(a)
