"""
Code in Place 2024 https://codeinplace.stanford.edu/cip4
My notes: https://github.com/egalli64/pythonesque/cip

Move if clear: put down a beeper in the next cell, if possible, or in the current one
"""

from stanfordkarel import *


def main():
    if front_is_clear():
        move()
    put_beeper()


if __name__ == "__main__":
    """
    Run python from the current directory
    """
    run_karel_program("8x1")
