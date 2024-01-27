"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

Logic 2: https://codingbat.com/python/Logic-2
make_chocolate: https://codingbat.com/prob/p190859
"""


def make_chocolate(small, big, goal):
    """
    Parameters:
        small int number of chunks sized 1
        big int number of chunks sized 5
        goal int
    Return minimal number of small needed to get goal, or -1 (not possible)
    """
    goal -= min(big * 5, goal - goal % 5)
    return goal if small >= goal else -1
