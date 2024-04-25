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
    """
    Precondition: Karel is on the bottom-left cell, facing East
    Postcondition: Karel is on the bottom-right cell, facing West
    """
    while front_is_clear():
        if beepers_present():
            build_hospital()
        if front_is_clear():
            move()


def build_hospital():
    """
    Karel builds a hospital

    Precondition: Karel is on a beeper, representing a pile of supplies, facing East
    Postcondition: Karel is standing at the bottom of the last column of the hospital, facing East
    """
    pick_beeper()
    build_column()
    move()
    build_column()


def build_column():
    """
    A hospital is done by two columns sized three

    Precondition: Karel is on a cell with a beeper, facing East
    Postcondition: Karel is in the same position, the column is placed
    """
    turn_left()
    for i in range(3):
        put_beeper()
        move()
    back_to_base()


def back_to_base():
    """
    Move Karel to the base row

    Precondition: Karel is facing North
    Postcondition: Karel is on the first row, facing East
    """
    turn_around()
    while front_is_clear():
        move()
    turn_left()


def turn_around():
    """
    Make Karel turn around
    """
    for i in range(2):
        turn_left()


if __name__ == "__main__":
    """
    Karel bootstrap
    """
    run_karel_program("hospital_karel")
