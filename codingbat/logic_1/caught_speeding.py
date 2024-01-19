"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

Logic 1: https://codingbat.com/python/Logic-1
caught_speeding: https://codingbat.com/prob/p137202
"""


def caught_speeding(speed, is_birthday):
    """
    Parameters:
        speed int
        is_birthday bool
    return an int in 0, 1, 2:
        0 if speed is not higher than 60,
        1 if speed is in [61, 80],
        2 if speed is above 80,
        but if is_birthday the limits are + 5
    """
    delta = is_birthday * 5
    if speed > 80 + delta:
        return 2
    elif speed > 60 + delta:
        return 1
    else:
        return 0
