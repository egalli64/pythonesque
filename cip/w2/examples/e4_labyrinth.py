"""
Code in Place 2025 https://codeinplace.stanford.edu/cip5
My notes: https://github.com/egalli64/pythonesque/cip

Labyrinth: Karel is in one dead end, move it to the other one
"""

from stanfordkarel import *


def main():
    while front_is_clear():
        move_to_wall()
        turn_if_possible()


def turn_if_possible():
    """
    Pre: front is not clear
    Post: front is clear, if possible
    """
    if left_is_clear():
        turn_left()
    if right_is_clear():
        turn_right()


def turn_right():
    for _ in range(3):
        turn_left()


def move_to_wall():
    while front_is_clear():
        move()


if __name__ == "__main__":
    """Run python from the current directory, see worlds directory"""
    run_karel_program("labyrinth")
