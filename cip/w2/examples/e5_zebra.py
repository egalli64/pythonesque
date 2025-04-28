"""
Code in Place 2025 https://codeinplace.stanford.edu/cip5
My notes: https://github.com/egalli64/pythonesque/cip

Zebra Crossing Karel: two columns of beepers, three empty columns, ...
"""

from stanfordkarel import *


def main():
    zebra()
    while front_is_clear():
        for _ in range(4):
            move()
        zebra()


def zebra():
    turn_left()
    column()

    next_zebra_column()
    column()

    turn_left()


def column():
    put_beeper()
    while front_is_clear():
        move()
        put_beeper()


def next_zebra_column():
    turn_right()
    move()
    turn_right()


def turn_right():
    for _ in range(3):
        turn_left()


if __name__ == "__main__":
    """Run python from the current directory"""
    run_karel_program("7x7")
