"""
Code in Place 2024 https://codeinplace.stanford.edu/cip4
My notes: https://github.com/egalli64/pythonesque/cip

Backflip: Let Karel turn left four times (in place)
"""

from stanfordkarel import *


def main():
    """
    Backflip Karel

    Precondition: Karel is facing east
    Postcondition: Karel is facing east
    """
    for i in range(4):
        turn_left()


if __name__ == "__main__":
    """
    Run python from the current directory
    """
    run_karel_program("1x1")
