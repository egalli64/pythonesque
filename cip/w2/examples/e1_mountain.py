"""
Code in Place 2025 https://codeinplace.stanford.edu/cip5
My notes: https://github.com/egalli64/pythonesque/cip

Mountain Karel: climb a mountain a put a beeper on top of it
"""

from stanfordkarel import *


def main():
    climb()
    put_beeper()
    descend()


def climb():
    """
    Pre: at the mountain West base
    Post: at the mountain top
    """
    while front_is_blocked():
        step_up()


def step_up():
    """
    Pre: facing a wall East
    Post: facing East
    """
    turn_left()
    move()
    turn_right()
    move()


def descend():
    """
    Pre: at the mountain top
    Post: at the mountain East base
    """
    while front_is_clear():
        step_down()


def step_down():
    """
    Pre: on a row > 1, facing East
    Post: on the row below, facing East
    """
    move()
    turn_right()
    move()
    turn_left()


def turn_right():
    for _ in range(3):
        turn_left()


if __name__ == "__main__":
    """Run python from the current directory, see worlds directory"""
    run_karel_program("mountain")
