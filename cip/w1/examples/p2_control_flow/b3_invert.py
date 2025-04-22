"""
Code in Place 2025 https://codeinplace.stanford.edu/cip5
My notes: https://github.com/egalli64/pythonesque/cip

Invert: swap beeper/no beeper for each cell in the current row
"""

from stanfordkarel import *


def main():
    swap_beeper()
    while front_is_clear():
        move()
        swap_beeper()


def swap_beeper():
    if beepers_present():
        pick_beeper()
    else:
        put_beeper()
    # the following syntax is not supported in CIP :(
    # pick_beeper() if beepers_present() else put_beeper()


if __name__ == "__main__":
    """
    Run python from the current directory
    """
    run_karel_program("invert")
