"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

Logic 2: https://codingbat.com/python/Logic-2
lone_sum: https://codingbat.com/prob/p143951
"""


def lone_sum(a, b, c):
    """
    Parameters:
        a int
        b int
        c int
    return the sum of the non-duplicated values among the parameters
    """
    result = a if a != b and a != c else 0
    result += b if b != a and b != c else 0
    result += c if c != a and c != b else 0

    return result
