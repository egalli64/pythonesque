"""
Karel the Robot - Learns Python

Source: https://compedu.stanford.edu/karel-reader/docs/python/en/intro.html
My notes: https://github.com/egalli64/pythonesque/cip/karel

Chapter 3: Decomposition
https://compedu.stanford.edu/karel-reader/docs/python/en/chapter4.html
"""
from stanfordkarel import *


def main():
    """Decomposition: short functions, focused on a single action, identified by a significative name"""
    move()
    fill_pothole()
    move()


# Fills the pothole beneath Karel's current position by
# placing a beeper on that corner. For this function to work
# correctly, Karel must be facing east immediately above the
# pothole. When execution is complete, Karel will have
# returned to the same square and will again be facing east.
def fill_pothole():
    """ Precondition: Karel is on a pothole facing east

        Karel fills the pothole with a beeper

        Postcondition: Karel is on the filled pothole facing east
    """
    turn_right()
    move()
    put_beeper()
    turn_around()
    move()
    turn_right()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def turn_around():
    turn_left()
    turn_left()


if __name__ == '__main__':
    # A 5x4 world, Karel starts from [1,2], there's a pothole in 2
    run_karel_program("cip_ch04")
