"""
Code in Place 2024 https://codeinplace.stanford.edu/cip4
My notes: https://github.com/egalli64/pythonesque/cip

Midpoint Karel:
    Place a beeper in the central cell in the first row of wichever world
    Assume the world is squared, or higher than wider
    If even sized, put the beeper in the left-central cell
"""

from stanfordkarel import *


def main():
    """
    Precondition: Karel is in (1, 1), facing East
    Postcondition: Karel is in central cell, over a beeper - no other marks in the world
    """
    fill_row()
    border_nibbling()

    # place Karel in the right place
    turn_around()
    move()
    if facing_west():
        turn_around()


def fill_row():
    """
    Precondition: Karel is in (1, 1), facing East
    Postcondition: Karel is in last cell, all the row is filled with beepers
    """
    put_beeper()
    while front_is_clear():
        move()
        put_beeper()


def border_nibbling():
    """ remove all the extra beepers """
    while front_is_clear():
        move()

    turn_around()
    while no_beepers_present():
        move()

    move()
    if beepers_present():
        turn_around()
        move()
        pick_beeper()
        turn_around()
        border_nibbling()


def turn_around():
    turn_left()
    turn_left()


if __name__ == "__main__":
    """
    Run python from the current directory
    """
    run_karel_program("5x3")
