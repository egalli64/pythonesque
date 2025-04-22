"""
Code in Place 2025 https://codeinplace.stanford.edu/cip5
My notes: https://github.com/egalli64/pythonesque/cip

Beeper Path: follow the path of beeper, stop on the first clear cell
"""

from stanfordkarel import *


def main():
    """
    Precondition: Karel is in (1, 1), facing East, on a beeper
    Postcondition: Karel is in (x, 1), facing East, on an empty cell
    """
    while beepers_present():
        move()


if __name__ == "__main__":
    """
    Run python from the current directory
    """
    run_karel_program("8x2")
