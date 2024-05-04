"""
Code in Place 2024 https://codeinplace.stanford.edu/cip4
My notes: https://github.com/egalli64/pythonesque/cip

Zig zag: put beepers in a zig-zag pattern
Expect two rows and an even number of columns
"""

from stanfordkarel import *


def main():
    while front_is_clear():
        zig_zag()
        move_next()


def zig_zag():
    put_beeper()
    turn_left()
    move()
    turn_right()
    move()
    put_beeper()


def move_next():
    turn_right()
    move()
    turn_left()
    if front_is_clear():
        move()


def turn_right():
    for i in range(3):
        turn_left()


if __name__ == "__main__":
    """Run python from the current directory"""
    run_karel_program("8x2")
