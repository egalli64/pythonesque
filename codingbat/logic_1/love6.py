"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

Logic 1: https://codingbat.com/python/Logic-1
love6: https://codingbat.com/prob/p100958
"""


def love6(a, b):
    """
    Parameters:
        a int
        b int
    return True if a, b, a+b, or a-b is 6
    """
    return a == 6 or b == 6 or a + b == 6 or abs(a - b) == 6
