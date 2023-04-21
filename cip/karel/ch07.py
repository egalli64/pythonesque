"""
Karel the Robot - Learns Python

Source: https://compedu.stanford.edu/karel-reader/docs/python/en/intro.html
My notes: https://github.com/egalli64/pythonesque/cip/karel

Chapter 7: If Statements
https://compedu.stanford.edu/karel-reader/docs/python/en/chapter7.html
"""
from stanfordkarel import *


def main():
    """Swap beepers on the row 1"""
    while front_is_clear():
        invert_beeper()
        move()
    invert_beeper()


def invert_beeper():
    """Pick a beeper up if present, put it down otherwise"""
    if beepers_present():
        pick_beeper()
    else:
        put_beeper()


if __name__ == '__main__':
    run_karel_program("cip_ch07")
