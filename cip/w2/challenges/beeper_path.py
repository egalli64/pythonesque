"""
Code in Place 2024 https://codeinplace.stanford.edu/cip4
My notes: https://github.com/egalli64/pythonesque/cip

Beeper Path: let Karel follow the linear beeper path
"""

from stanfordkarel import *


def main():
    """
    Precondition: Karel is in (1, 1), facing East
    Postcondition: Karel is in the first clear cell on row 1
    """
    while beepers_present():
        move()


if __name__ == "__main__":
    """
    Run python from the current directory
    """
    run_karel_program("beeper_path")
