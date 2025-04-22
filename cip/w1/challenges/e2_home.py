"""
Code in Place 2025 https://codeinplace.stanford.edu/cip5
My notes: https://github.com/egalli64/pythonesque/cip

Karel's home: Pick the beeper, get back home, beware of walls!
"""

from stanfordkarel import *


def main():
    """
    Precondition: Karel is in (2, 4), facing East, a beeper is in (5, 3)
    Postcondition: Karel is in (2, 4), facing East, no beeper around
    """
    move()
    turn_right()
    move()
    turn_left()
    # reach the beeper and pick it up
    move()
    move()
    pick_beeper()
    # back home
    turn_around()
    move()
    move()
    move()
    turn_right()
    move()
    turn_right()


def turn_right():
    """
    Karel does not know how to turn right!
    """
    for i in range(3):
        turn_left()


def turn_around():
    """
    Karel can only turn left!
    """
    for i in range(2):
        turn_left()


if __name__ == "__main__":
    """
    Run python from the current directory, see the worlds/warmup.w
    """
    run_karel_program("home")
