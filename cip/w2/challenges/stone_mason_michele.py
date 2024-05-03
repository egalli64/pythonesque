"""
Code in Place 2024 https://codeinplace.stanford.edu/cip4
My notes: https://github.com/egalli64/pythonesque/cip

Stone Mason Karel: build beeper columns up to the roof, distanced 4
Michele version - after fix
"""
from stanfordkarel import *


def main():
    build_column()
    while front_is_clear():
        move_next()
        build_column()


def build_column():
    turn_left()
    for i in range(4):
        move()
    turn_around()
    put_beeper()
    for i in range(4):
        move()
        put_beeper()
    turn_left()


def move_next():
    for i in range(4):
        move()


def turn_around():
    for i in range(2):
        turn_left()


if __name__ == "__main__":
    """
    Run python from the current directory, see the worlds folder
    """
    run_karel_program("stone_mason")
