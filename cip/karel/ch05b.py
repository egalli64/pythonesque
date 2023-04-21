"""
Karel the Robot - Learns Python

Source: https://compedu.stanford.edu/karel-reader/docs/python/en/intro.html
My notes: https://github.com/egalli64/pythonesque/cip/karel

Chapter 5: For Loops (b) Matching Postconditions with Preconditions
https://compedu.stanford.edu/karel-reader/docs/python/en/chapter5.html
"""
from stanfordkarel import *


def main():
    """Put a beeper in each corner of a world"""

    # repeat the body 4 times
    for i in range(4):
        # Precondition: Karel is in a corner with no beeper in it, pointing to the next corner to be reached
        put_beeper()
        move()
        move()
        move()
        move()
        turn_left()  # what if this line is commented out?
        # Postcondition: same as precondition - but the last iteration, when the corner has a beeper in it


if __name__ == '__main__':
    # A 5x5 world, Karel starts from [1,1]
    run_karel_program("5x5")
