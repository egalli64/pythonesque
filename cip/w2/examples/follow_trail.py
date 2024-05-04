"""
Code in Place 2024 https://codeinplace.stanford.edu/cip4
My notes: https://github.com/egalli64/pythonesque/cip

Follow trail: pick any beeper in the trail
- the trail starts from (1, 1) leading East
- no trail segment leads to crash in a wall
"""

from stanfordkarel import *


def main():
    """
    Pre: in (1, 1), facing East
    Post: in the first cell after the trail, facing the right direction
    """
    while beepers_present():
        follow_straight_trail()
        check_for_split()


def follow_straight_trail():
    while beepers_present():
        pick_beeper()
        move()
    step_backwards()


def check_for_split():
    """
    Pre: on the trail
    Post: on the trail leading left or right, or on the first right cell out of the trail
    """
    # check left
    turn_left()
    move()
    if no_beepers_present():
        # no trail on left, check right
        step_backwards()
        turn_around()
        move()


def step_backwards():
    """
    Pre: on a cell in the world
    Post: move back, keep the same direction in "pre"
    """
    turn_around()
    move()
    turn_around()


def turn_around():
    for i in range(2):
        turn_left()


if __name__ == "__main__":
    """
    Run python from the current directory, see worlds directory
    """
    run_karel_program("follow_trail")
