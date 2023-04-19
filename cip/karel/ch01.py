"""
Karel the Robot - Learns Python

Source: https://compedu.stanford.edu/karel-reader/docs/python/en/intro.html
My notes: https://github.com/egalli64/pythonesque/cip/karel

Chapter 1: Introducing Karel the Robot
https://compedu.stanford.edu/karel-reader/docs/python/en/chapter1.html
"""
# see https://pypi.org/project/stanfordkarel/
from stanfordkarel import *


def main():
    """The user startup function"""

    # move forward one block, when possible
    move()
    # take a beeper from the bag and put it down on the current corner
    put_beeper()

    move()

    # rotate 90 degrees to the left (counterclockwise)
    turn_left()

    # going back
    turn_left()
    move()

    # pick up one beeper from a corner and stores it in its bag
    pick_beeper()

    move()

    # reset position
    turn_left()
    turn_left()


if __name__ == '__main__':
    # setup of Karel world
    run_karel_program()
