"""
Code in Place 2024 https://codeinplace.stanford.edu/cip4
My notes: https://github.com/egalli64/pythonesque/cip

Clean Up Karel: pick any beeper in the current world
"""

from stanfordkarel import *


def main():
    """
    Pre: in (1, 1), facing East
    Post: in rightmost topmost cell, facing East
    """
    while left_is_clear():
        pick_row()
        back_to_first()
        move_up()
        turn_right()

    pick_row()


def pick_row():
    """
    Pick up a row of beepers

    Pre: in the leftmost cell in a row, facing East
    Post: in the rightmost cell in a row, facing East
    """
    while front_is_clear():
        if beepers_present():
            pick_beeper()
        move()

    if beepers_present():
        pick_beeper()


def back_to_first():
    """
    Move back to the first column

    Pre: facing East
    Post: facing West
    """
    turn_around()
    move_to_wall()


def move_up():
    """
    Move up to the next row

    Pre: facing West
    Post:facing North
    """
    turn_right()
    move()


def move_to_wall():
    while front_is_clear():
        move()


def turn_around():
    for i in range(2):
        turn_left()


def turn_right():
    for i in range(3):
        turn_left()


if __name__ == "__main__":
    """
    Run python from the current directory, see worlds directory
    """
    run_karel_program("clean_spot")
