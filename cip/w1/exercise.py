"""
Code in Place 2023-2024 https://codeinplace.stanford.edu/cip4
My notes: https://github.com/egalli64/pythonesque/cip

Section Week 1: Hospital Karel
- See the standard world hospital_karel.w for the initial setup
- Karel's job is to walk along the row and build a new hospital in the places marked by each beeper
- Each hospital should be two columns of three beepers
"""

from stanfordkarel import *


def main():
    # Karel starts its trip from bottom-left, with right direction
    while front_is_clear():
        if beepers_present():
            build_hospital()
        if front_is_clear():
            move()


def build_hospital():
    """
    Karel builds a hospital

    Pre-condition: Karel is on a beeper, representing a pile of supplies. Karel is facing east
    Post-condition: Karel is standing at the bottom of the last column of the hospital, facing east
    """
    pick_beeper()
    build_column()
    move()
    build_column()


def build_column():
    """
    A hospital is done by two columns sized three

    Precondition: Karel is on a beeper, directed to east
    Postcondition: Karel is in the original position, the first column is placed
    """
    turn_left()
    for i in range(3):
        put_beeper()
        move()
    back_to_base()


def back_to_base():
    """
    Move Karel to the base row

    Precondition: Karel is directed north
    Postcondition: Karel is on the first row, directed east
    """
    turn_around()
    while front_is_clear():
        move()
    turn_left()


def turn_around():
    """
    Make Karel turn around
    """
    turn_left()
    turn_left()


if __name__ == "__main__":
    """
    Karel bootstrap
    """
    run_karel_program("hospital_karel")
