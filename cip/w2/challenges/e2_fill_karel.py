"""
Code in Place 2025 https://codeinplace.stanford.edu/cip5
My notes: https://github.com/egalli64/pythonesque/cip

Fill Karel: fill whichever world with beepers
"""

from stanfordkarel import *


def main():
    """
    Precondition: Karel is in (1, 1), facing East
    Postcondition: Karel is in the right topmost cell, facing East
    """
    while left_is_clear():
        fill_row()
        next_row()
    fill_row()


def fill_row():
    """
    Fill the corrent row with beepers

    Precondition: Karel is on first column, facing East
    Postcondition: Karel is on last column, facing East
    """
    put_beeper()
    while front_is_clear():
        move()
        put_beeper()

def next_row():
    """
    Precondition: Karel is on last column, facing East
    Postcondition: Karel is on first column in the row above, facing East
    """
    turn_back()
    while front_is_clear():
        move()

    turn_right()
    move()
    turn_right()


def turn_back():
    turn_left()
    turn_left()


def turn_right():
    for i in range(3):
        turn_left()


if __name__ == "__main__":
    """
    Run python from the current directory
    """
    run_karel_program("5x5")
