"""
Code in Place 2025 https://codeinplace.stanford.edu/cip5
My notes: https://github.com/egalli64/pythonesque/cip

Spring flowers: there are two stems, put four beepers on top of them
"""

from stanfordkarel import *


def main():
    for _ in range(2):
        move_to_wall()
        climb()
        bloom()
        move_down()
    move_to_wall()


def climb():
    turn_left()
    while right_is_blocked():
        move()


def move_down():
    move_to_wall()
    turn_left()


def bloom():
    for _ in range(2):
        put_beeper()
        move()

    for _ in range(2):
        turn_right()
        move()

    for _ in range(2):
        put_beeper()
        move()


def move_to_wall():
    while front_is_clear():
        move()


def turn_right():
    for _ in range(3):
        turn_left()


if __name__ == "__main__":
    """Run python from the current directory, see worlds directory"""
    run_karel_program("spring")
