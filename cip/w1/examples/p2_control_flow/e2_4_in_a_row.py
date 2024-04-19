"""
Code in Place 2024 https://codeinplace.stanford.edu/cip4
My notes: https://github.com/egalli64/pythonesque/cip

4 in a row: place 4 beepers on each cell from the current one
"""

from stanfordkarel import *


def main():
    """
    Place four beepers in a row

    Precondition: Karel is facing east, there is room for four beepers
    Postcondition: Karel is in the last placed beeper, facing east
    """
    put_beeper()
    for i in range(3):
        move()
        put_beeper()


if __name__ == "__main__":
    """
    Run python from the current directory
    """
    run_karel_program("8x1")
