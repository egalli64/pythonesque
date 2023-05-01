"""
Code in Place 2023 https://codeinplace.stanford.edu/cip3
My notes: https://github.com/egalli64/pythonesque/cip

Week 2: Fill Karel
- An empty world. Karel is on (1,1), facing east
- No matter the size of the world, Karel should fill it with beepers
"""
from stanfordkarel import *


def main():
    # Karel starts its trip from bottom-left, with right direction
    while left_is_clear():
        fill_current_row()
        move_back()
        move_up()
    fill_current_row()


def fill_current_row():
    """
    Pre-condition: Karel is on the first corner of the row, facing east.
    Post-condition: Karel is on the last corner of the row, facing east.
    """
    while front_is_clear():
        put_beeper()
        move()
    put_beeper()


def move_back():
    """
    Pre-condition: Karel is on the last corner of the row, facing east.
    Post-condition: Karel is on the first corner of the row, facing west.
    """
    turn_back()
    while front_is_clear():
        move()


def move_up():
    turn_right()
    move()
    turn_right()


def turn_back():
    turn_left()
    turn_left()


def turn_right():
    for _ in range(3):
        turn_left()


if __name__ == '__main__':
    run_karel_program()
