"""
Code in Place 2024 https://codeinplace.stanford.edu/cip4
My notes: https://github.com/egalli64/pythonesque/cip

Stone Mason Karel: build beeper columns up to the roof, distanced 4
"""

from stanfordkarel import *


def main():
    """
    Precondition: Karel is in (1, 1), facing East
    Postcondition: Karel is in (13, 1), facing East
    """
    build_column()
    while front_is_clear():
        move_next()
        build_column()


def build_column():
    """
    Precondition: Karel is on position, facing East
    Postcondition: Karel is on same position, facing East
    """
    turn_left()
    put_beeper()
    while front_is_clear():
        move()
        put_beeper()

    turn_back()
    while front_is_clear():
        move()
    turn_left()


def move_next():
    for i in range(4):
        move()


def turn_back():
    turn_left()
    turn_left()


if __name__ == "__main__":
    """
    Run python from the current directory, see the worlds folder
    """
    run_karel_program("stone_mason")
