"""
Code in Place 2024 https://codeinplace.stanford.edu/cip4
My notes: https://github.com/egalli64/pythonesque/cip

Five corridors: ensure each row has a single beeper at its end
"""

from stanfordkarel import *


def main():
    """
    Precondition: Karel is in (1, 1), facing east
    Postcondition: Karel is in (1, 5), facing east, beepers are placed as required
    """
    for i in range(4):
        check_corridor()
        move_up()
    check_corridor()


def check_corridor():
    """
    If no beeper is in the rightmost cell, place it
    Precondition: Karel is in the leftmost cell, facing east
    Postcondition: Karel is in the leftmost cell, facing east
    """
    move_to_wall()
    if no_beepers_present():
        put_beeper()
    turn_back()
    move_to_wall()
    turn_back()


def move_to_wall():
    while front_is_clear():
        move()


def move_up():
    turn_left()
    move()
    for i in range(3):
        turn_left()


def turn_back():
    turn_left()
    turn_left()


if __name__ == "__main__":
    """
    Run python from the current directory
    """
    run_karel_program("five_corridors")
