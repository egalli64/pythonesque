"""
Code in Place 2023 https://codeinplace.stanford.edu/cip3
My notes: https://github.com/egalli64/pythonesque/cip

Section Week 2: Spread Beepers
- Custom world. Karel is on (1,1), facing east
- There is a pile of beepers on (2,1), Karel has to spread them out along the row
"""
from stanfordkarel import *


def main():
    # We know for sure the pile is on (1,1)
    move()
    # Do the actual job
    spread()
    # Back to starting position
    back_home()


def spread():
    """ Spread the beepers in the current position on the right ones"""

    while beepers_present():
        pick_beeper()
        if beepers_present():
            move_to_first_free()
            put_beeper()
            back_to_pile()

    # When the pile is done, place back a beeper on the starting place
    put_beeper()


def move_to_first_free():
    """Move until a free place is seen"""
    while beepers_present():
        move()


def back_to_pile():
    """Move back to the pile"""
    turn_around()
    move_to_first_free()
    turn_around()
    move()


def turn_around():
    """Utility function"""
    turn_left()
    turn_left()


def back_home():
    """Move from the pile (2,1) to the Karel starting position (1,1)"""
    turn_around()
    move()
    turn_around()


if __name__ == '__main__':
    run_karel_program("cip_w2_7")
