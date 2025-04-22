"""
Code in Place 2025 https://codeinplace.stanford.edu/cip4
Adapted for https://pypi.org/project/stanfordkarel/
My notes: https://github.com/egalli64/pythonesque/cip

Step up: remove a beeper from (2, 1), and put one in (4, 2), beware of walls
"""

from stanfordkarel import *


def main():
    """
    Precondition: Karel is in (1, 1) facing East
    Postcondition: Karel is in (5, 2) facing East
    """
    move()
    pick_beeper()
    move()
    turn_left()
    move()
    turn_right()
    move()
    put_beeper()
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
    run_karel_program("step_up")
