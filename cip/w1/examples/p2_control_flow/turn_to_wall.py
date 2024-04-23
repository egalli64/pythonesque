"""
Code in Place 2024 https://codeinplace.stanford.edu/cip4
My notes: https://github.com/egalli64/pythonesque/cip

Turn to wall: turn until you see a wall
"""

from stanfordkarel import *


def main():
    while front_is_clear():
        turn_left()


if __name__ == "__main__":
    """
    Run python from the current directory
    """
    run_karel_program("2x2")
