"""
Code in Place 2024 https://codeinplace.stanford.edu/cip4
My notes: https://github.com/egalli64/pythonesque/cip

Obstacles: put beepers in the first row, column 3, 4, and 5 - but avoid walls!
"""

from stanfordkarel import *


def main():
    """
    Precondition: Karel is in (1, 1) facing East
    Postcondition: Karel is in (7, 1) facing East
    """
    move()

    for i in range(3):
        jump()
        put_beeper()

    move()
    move()


def jump():
    """
    Move Karel to the next East cell, passing from the cells above

    Precondition: Karel faces East, the row above is clear
    Postcondition: Karel is on the next cell on the same row, facing East
    """
    turn_left()
    move()
    for i in range(2):
        turn_right()
        move()
    turn_left()


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
    run_karel_program("obstacles")
