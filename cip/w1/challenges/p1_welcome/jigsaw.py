"""
Code in Place 2024 https://codeinplace.stanford.edu/cip4
My notes: https://github.com/egalli64/pythonesque/cip

Jigsaw Karel: pick a beeper in position (3, 1) and put it in (4, 3)
"""

from stanfordkarel import *


def main():
    """
    Precondition: Karel is in (1, 1), facing East, a beeper is in (3, 1)
    Postcondition: Karel is in (1, 1), facing East, the beeper now is in (4, 3)
    """
    get_piece()
    put_piece()
    back_home()


def get_piece():
    move()
    move()
    pick_beeper()


def put_piece():
    move()
    turn_left()
    move()
    move()
    put_beeper()


def back_home():
    turn_around()
    move()
    move()
    turn_right()
    move()
    move()
    move()
    turn_around()


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
    Run python from the current directory, see the worlds folder
    """
    run_karel_program("jigsaw")
