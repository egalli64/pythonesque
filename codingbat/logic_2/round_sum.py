"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

Logic 2: https://codingbat.com/python/Logic-2
round_sum: https://codingbat.com/prob/p179960
"""


def round_sum(a, b, c):
    """
    Parameters:
        a int
        b int
        c int
    Return the sum of rounded to ten parameters
    """
    return round10(a) + round10(b) + round10(c)


def round10(num):
    """
    Rounding to ten, ex: 14 to 10; 25 to 30
    """
    unity = num % 10
    delta = -unity if unity < 5 else 10 - unity
    return num + delta
