"""
Karel the Robot - Learns Python

Source: https://compedu.stanford.edu/karel-reader/docs/python/en/intro.html
My notes: https://github.com/egalli64/pythonesque/cip/karel

Chapter 5: For Loops (c) Nested Loops
https://compedu.stanford.edu/karel-reader/docs/python/en/chapter5.html
"""
from stanfordkarel import *


def main():
    """Put five beeper in each corner of a world"""

    # For each corner
    for i in range(4):
        put_five_beepers()
        move_to_next_corner()


def move_to_next_corner():
    move()
    move()
    move()
    move()
    turn_left()


def put_five_beepers():
    for i in range(5):
        put_beeper()


if __name__ == '__main__':
    run_karel_program("5x5")
