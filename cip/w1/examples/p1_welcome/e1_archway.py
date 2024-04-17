"""
Code in Place 2024 https://codeinplace.stanford.edu/cip4
My notes: https://github.com/egalli64/pythonesque/cip

Archway: move Karel from (1, 1) to (4, 1) - but notice the walls in the current world!
"""

from stanfordkarel import *


def main():
    """
    Precondition: Karel is in (1, 1) and directed east
    Postcondition: Karel is in (4, 1) and directed east
    """
    # move North
    turn_left()
    move_x3()

    # move East
    turn_right()
    move_x3()

    # move South
    turn_right()
    move_x3()

    # as for requirement
    turn_left()


def move_x3():
    """
    An unflexible way to move to the end of the corridor
    """
    for i in range(3):
        move()


def turn_right():
    """
    Karel does not know how to turn right!
    """
    for i in range(3):
        turn_left()


if __name__ == "__main__":
    """
    Run python from the current directory, see the worlds folder
    """
    run_karel_program("archway")
