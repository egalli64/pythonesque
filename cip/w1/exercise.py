"""
Code in Place 2023 https://codeinplace.stanford.edu/cip3
My notes: https://github.com/egalli64/pythonesque/cip

Section Week 1: Hospital Karel
- See the standard world hospital_karel.w for the initial setup
- Karel's job is to walk along the row and build a new hospital in the places marked by each beeper.
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
    Karel builds a hospital.
    Pre-condition: Karel is on a beeper, representing a
        pile of supplies. Karel is facing east.
    Post-condition: Karel is standing at the bottom
        of the last column of the hospital, facing east.
    """
    turn_left()
    build_section()
    turn_right()
    move()
    put_beeper()
    turn_right()
    build_section()
    turn_left()


def build_section():
    """
    We can see a hospital as two columns made of a beeper plus a two beepers in the same row.
    A section is this pair of beepers.
    Precondition: Karel is on a beeper, need to put down a section in its current direction
    Postcondition: Karel is in the same direction, has moved and placed two beepers
    """
    for i in range(2):
        move()
        put_beeper()


def turn_right():
    for i in range(3):
        turn_left()


if __name__ == '__main__':
    run_karel_program("hospital_karel")
