"""
Code in Place 2024 https://codeinplace.stanford.edu/cip4
My notes: https://github.com/egalli64/pythonesque/cip

Invert spot: swap beeper/no beeper for the current cell
"""

from stanfordkarel import *


def main():
    if beepers_present():
        pick_beeper()
    else:
        put_beeper()


if __name__ == "__main__":
    """
    Run python from the current directory
    """
    run_karel_program("1x1")
