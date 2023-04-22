"""
Karel the Robot - Learns Python

Source: https://compedu.stanford.edu/karel-reader/docs/python/en/intro.html
My notes: https://github.com/egalli64/pythonesque/cip/karel

Chapter 8: Stepwise Refinement /3
https://compedu.stanford.edu/karel-reader/docs/python/en/chapter8.html

The Problem:
On each of the columns, there is a tower of beepers of an unknown height (could be 0)
Karel starts with an empty beeper bag, in position (1, 1), facing east and it has to:
    - collect all beepers in each tower
    - put them on the easternmost corner of 1st row
    - return to its starting position
"""
from stanfordkarel import *


def main():
    """ Precondition: Karel is on its starting place

        Solve the problem

        Postcondition: Karel is back to its starting place
    """
    collect_all_beepers()
    drop_all_beepers()
    return_home()


def collect_all_beepers():
    """ Precondition: Karel is on its starting place

        Collect all the beepers

        Postcondition: Karel is eastmost position on row 1, facing east
    """
    print("Collecting beepers")
    while front_is_clear():
        collect_current_tower()
        move()
    # forgetting this last step would be a bug!
    collect_current_tower()


def collect_current_tower():
    """ Precondition: Karel is on row 1 in a column, facing east

        Collect all the beepers in the column - no hole expected in the tower

        Postcondition: Karel is in the same position as precondition
    """
    if beepers_present():
        turn_left()
        collect_beeper_line()
        turn_around()
        move_to_wall()
        turn_left()
    else:
        print("No tower here")


def collect_beeper_line():
    """ Precondition: Karel should have a wall at its back, and is on the beginning of a beeper sequence

        Peek all the beeper on until an empty corner is found

        Postcondition: Karel is on an empty corner
    """
    while beepers_present():
        pick_beeper()
        if front_is_clear():
            move()
    print("Line of beepers collected")


def drop_all_beepers():
    print("Dropping beepers")


def return_home():
    turn_around()
    move_to_wall()
    turn_around()
    print("Back home")


def turn_around():
    """Helper to turn around Karel"""
    turn_left()
    turn_left()


def move_to_wall():
    """Helper to move Karel on until reaching the wall"""
    while front_is_clear():
        move()


if __name__ == '__main__':
    # A 9x7 world with towers of beepers raising from floor 1
    run_karel_program("cip_ch08")
