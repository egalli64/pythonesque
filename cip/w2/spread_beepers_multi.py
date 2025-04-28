"""
Code in Place 2025 https://codeinplace.stanford.edu/cip5
My notes: https://github.com/egalli64/pythonesque/cip

Section Week 2: Spread Beepers - extra
- Karel is on (1,1), facing East
- There are piles of beepers on (2, x), where x is each row of the world
- Karel has to spread them out along the row
- Karel can't count! Each beeper has to be placed in the first available empty cell
"""

from stanfordkarel import *


def main():
    """
    Pre: in (1, 1) facing East
    Post: in (1, 1) facing East
    """
    while left_is_clear():
        current_row()
        next_row()
    current_row()


def current_row():
    """
    Pre: first cell in the current row, facing East
    Post: first cell in the current row, in (1, 1) facing East
    """
    # We know for sure the pile is on (2, 1)
    move()
    # Do the actual job
    spread()
    # Back to starting position
    back_home()


def next_row():
    turn_left()
    move()
    turn_right()


def spread():
    """
    Spread the beepers in the current position on the right ones

    Pre: on the pile, facing East
    Post: on the pile, facing East
    """

    while beepers_present():
        pick_beeper()
        if beepers_present():
            move_to_first_free()
            put_beeper()
            back_to_pile()

    # When the pile is done, place back a beeper on the starting place
    put_beeper()


def move_to_first_free():
    """
    Move ahead until a free place is seen

    It is assumed there is place where to move
    """
    while beepers_present():
        move()


def back_to_pile():
    """
    Move back to the first beeper in the row

    Pre: facing East
    Post: facing East
    """
    turn_around()
    move_to_first_free()
    turn_around()
    move()


def turn_around():
    for _ in range(2):
        turn_left()


def turn_right():
    for _ in range(3):
        turn_left()


def back_home():
    """
    Pre: on (2,1) facing East
    Post: on (1,1) facing East
    """
    turn_around()
    move()
    turn_around()


if __name__ == "__main__":
    run_karel_program("exercise_extra")
