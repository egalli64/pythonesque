"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

Logic 2: https://codingbat.com/python/Logic-2
make_bricks: https://codingbat.com/prob/p118406
"""


def make_bricks(small, big, goal):
    """
    Parameters:
        small int, number of bricks size 1
        big int, number of bricks sized 5
        goal int, total size aimed to reach with the passed bricks
    return True if it is possible to reach the goal given the passed bricks
    """
    return goal <= big * 5 + small and goal % 5 <= small
