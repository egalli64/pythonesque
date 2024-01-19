"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

Logic 1: https://codingbat.com/python/Logic-1
date_fashion: https://codingbat.com/prob/p129125
"""


def date_fashion(you, date):
    """
    Parameters:
        you int in [0..10]
        date int in [0..10]
    return int:
        if either is 8+ then 2,
        but if either is 2- then 0,
        otherwise 1
    """
    if you <= 2 or date <= 2:
        return 0
    else:
        return 2 if you >= 8 or date >= 8 else 1
