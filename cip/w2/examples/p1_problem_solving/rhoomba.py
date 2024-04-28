"""
Code in Place 2024 https://codeinplace.stanford.edu/cip4
My notes: https://github.com/egalli64/pythonesque/cip

Rhoomba: pick up every beeper in the world
At the end Karel should be facing East at the top right corner of a world with zero beepers left
"""

from stanfordkarel import *


def main():
    while left_is_clear():
        clear_row()
        next_row()
    clear_row()


def clear_row():
    """
    Pre: on leftmost cell, facing East
    Post: on rightmost cell, facing East
    """
    while front_is_clear():
        safe_pick_beeper()
        move()
    safe_pick_beeper()


def safe_pick_beeper():
    if beepers_present():
        pick_beeper()


def next_row():
    """
    Pre: on rightmost cell, facing East
    Post: on the row above, first cell, facing East
    """
    turn_around()
    move_to_wall()
    turn_right()
    move()
    turn_right()


def move_to_wall():
    while front_is_clear():
        move()


def turn_right():
    for i in range(3):
        turn_left()


def turn_around():
    for i in range(2):
        turn_left()


if __name__ == "__main__":
    """Run python from the current directory, see worlds directory"""
    run_karel_program("rhoomba")
