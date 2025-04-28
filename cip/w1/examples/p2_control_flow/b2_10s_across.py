"""
Code in Place 2025 https://codeinplace.stanford.edu/cip5
My notes: https://github.com/egalli64/pythonesque/cip

10s across the board: place 10 beepers on each cell on the first row
"""

# alternative import
# from karel.stanfordkarel import *

from stanfordkarel import *


def main():
    """
    Fill the current row with 10 beeper in each cell

    Precondition: Karel is in (1, 1), facing east
    Postcondition: Karel is in the last cell of the row, facing east
    """
    put_10_beepers()
    while front_is_clear():
        move()
        put_10_beepers()


def put_10_beepers():
    for i in range(10):
        put_beeper()


if __name__ == "__main__":
    """
    Run python from the current directory
    """
    run_karel_program("5x3")
