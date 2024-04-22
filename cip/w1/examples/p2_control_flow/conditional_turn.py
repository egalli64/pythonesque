"""
Code in Place 2024 https://codeinplace.stanford.edu/cip4
My notes: https://github.com/egalli64/pythonesque/cip

Conditional turn: turn right if there is a beeper, otherwise turn left
"""

from stanfordkarel import *


def main():
    turn_left()
    if no_beepers_present():
        turn_left()
        turn_left()


if __name__ == "__main__":
    """
    Run python from the current directory
    """
    run_karel_program("clean_spot")
