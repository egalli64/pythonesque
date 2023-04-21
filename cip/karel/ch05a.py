"""
Karel the Robot - Learns Python

Source: https://compedu.stanford.edu/karel-reader/docs/python/en/intro.html
My notes: https://github.com/egalli64/pythonesque/cip/karel

Chapter 5: For Loops (a) simple
https://compedu.stanford.edu/karel-reader/docs/python/en/chapter5.html
"""
from stanfordkarel import *


def main():
    """Go to (2,1), place 6 beeper, then move to (3,1)"""
    move()
    # repeat put_beeper many times
    for i in range(6):
        put_beeper()
    move()


if __name__ == '__main__':
    # A 5x5 world, Karel starts from [1,1]
    run_karel_program("5x5")
