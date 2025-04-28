"""
Code in Place 2025 https://codeinplace.stanford.edu/cip5
My notes: https://github.com/egalli64/pythonesque/cip

Checkerboard Karel: create a checkerboard pattern
"""

from stanfordkarel import *


def main():
    put_beeper()
    fill_row()
    while left_is_clear():
        next_row()
        fill_row()
    back_col()


def fill_row():
    while front_is_clear():
        if beepers_present():
            move()
        if front_is_clear():
            move()
            put_beeper()
    back_row()


def back_row():
    turn_around()
    while front_is_clear():
        move()
    turn_around()


def back_col():
    turn_right()
    while front_is_clear():
        move()
    turn_left()


def next_row():
    turn_left()
    if beepers_present():
        move()
    else:
        move()
        put_beeper()
    turn_right()


def turn_around():
    for i in range(2):
        turn_left()


def turn_right():
    for i in range(3):
        turn_left()


if __name__ == "__main__":
    """
    Run python from the current directory
    """
    run_karel_program("8x8")
