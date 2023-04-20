"""
Karel the Robot - Learns Python

Source: https://compedu.stanford.edu/karel-reader/docs/python/en/intro.html
My notes: https://github.com/egalli64/pythonesque/cip/karel

Chapter 3: Defining New Functions
https://compedu.stanford.edu/karel-reader/docs/python/en/chapter3.html
"""
from stanfordkarel import *


def main():
    """Same as ch02, with improved custom turn_right command"""
    # 1. pick the beeper in [2, 1]
    move()
    pick_beeper()

    # 2. put the beeper in [5, 2]
    move()
    turn_left()
    move()
    turn_right()
    move()
    move()
    put_beeper()

    # 3. move to the last row
    move()


def turn_right():
    """karel has no built-in turn right command"""
    turn_left()
    turn_left()
    turn_left()


def turn_around():
    """karel has no built-in go back command"""
    turn_left()
    turn_left()


if __name__ == '__main__':
    # A 6x4 world , with a beeper in [2, 1], west and north wall in [4, 1], north walls in [5 and 6, 1]
    run_karel_program("cip_ch02")
