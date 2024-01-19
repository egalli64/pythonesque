"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

Logic 1: https://codingbat.com/python/Logic-1
squirrel_play: https://codingbat.com/prob/p135815
"""


def squirrel_play(temp, is_summer):
    """
    Parameters:
        temp int
        is_summer bool
    return True temp is in [60 .. 90] or, if is_summer, 100 as upper limit
    """
    return 60 <= temp <= 90 + 10 * is_summer
