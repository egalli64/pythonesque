"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

Warmup 1 https://codingbat.com/python/Warmup-1
front3 https://codingbat.com/prob/p147920
"""


def front3(str):
    """
    Parameter:
        str a non-empty string
    return three times the first three chars (or less) from str
    """
    return str[:3] * 3
