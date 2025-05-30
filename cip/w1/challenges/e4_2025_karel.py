"""
Code in Place 2025 https://codeinplace.stanford.edu/cip5
My notes: https://github.com/egalli64/pythonesque/cip

2025 Karel: place 20 and 25 beepers in first and second cell of the first row, then Karel
"""

from stanfordkarel import *


def main():
    """
    Precondition: Karel is in (1, 1), facing East
    Postcondition: Karel is in (3, 1), facing East, with 20 and 24 beepers before
    """
    for i in range(20):
        put_beeper()
    move()

    for i in range(25):
        put_beeper()
    move()


if __name__ == "__main__":
    """
    Run python from the current directory
    """
    run_karel_program("5x3")
