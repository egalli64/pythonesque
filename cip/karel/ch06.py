"""
Karel the Robot - Learns Python

Source: https://compedu.stanford.edu/karel-reader/docs/python/en/intro.html
My notes: https://github.com/egalli64/pythonesque/cip/karel

Chapter 6: While Loops
https://compedu.stanford.edu/karel-reader/docs/python/en/chapter6.html
"""
from stanfordkarel import *


def main():
    # A Basic While Loop
    move_to_wall()
    turn_left()

    # The Fencepost Bug
    build_fence_bug()
    turn_left()

    move_to_wall()
    turn_left()

    # The Fencepost Bug Solved
    build_fence()
    turn_left()


def move_to_wall():
    while front_is_clear():
        move()


def build_fence_bug():
    while front_is_clear():
        put_beeper()
        move()


def build_fence():
    while front_is_clear():
        put_beeper()
        move()
    # solves the fencepost bug
    put_beeper()


if __name__ == '__main__':
    run_karel_program("7x7")
