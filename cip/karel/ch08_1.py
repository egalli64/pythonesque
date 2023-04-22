"""
Karel the Robot - Learns Python

Source: https://compedu.stanford.edu/karel-reader/docs/python/en/intro.html
My notes: https://github.com/egalli64/pythonesque/cip/karel

Chapter 8: Stepwise Refinement
https://compedu.stanford.edu/karel-reader/docs/python/en/chapter8.html

The Problem:
On each of the columns, there is a tower of beepers of an unknown height (could be 0)
Karel starts with an empty beeper bag, in position (1, 1), facing east and it has to:
    - collect all beepers in each tower
    - put them on the easternmost corner of 1st row
    - return to its starting position
"""
from stanfordkarel import *


def main():
    """First implementation: just the solution structure"""
    collect_all_beepers()
    drop_all_beepers()
    return_home()


def collect_all_beepers():
    print("Collecting beepers")


def drop_all_beepers():
    print("Dropping beepers")


def return_home():
    print("Going back home")


if __name__ == '__main__':
    # A 9x7 world with towers of beepers raising from floor 1
    run_karel_program("cip_ch08")
