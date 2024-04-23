"""
Code in Place 2024 https://codeinplace.stanford.edu/cip4
My notes: https://github.com/egalli64/pythonesque/cip

Three slots: Karel is on the top left corner, put a beeper in each cell of the first row
Walls could be block the horizontal moves on the bottom row
"""

from stanfordkarel import *


def main():
    """
    Should world for a (3, 2) world, here I'm using a generic algorithm
    """
    while front_is_clear():
        fix_column()
        move()
    fix_column()


def fix_column():
    go_down()
    put_beeper()
    go_up()


def go_down():
    turn_right()
    while front_is_clear():
        move()


def go_up():
    turn_around()
    while front_is_clear():
        move()
    turn_right()


def turn_right():
    for i in range(3):
        turn_left()


def turn_around():
    for i in range(2):
        turn_left()


if __name__ == "__main__":
    """
    Run python from the current directory
    """
    run_karel_program("three_slots")
