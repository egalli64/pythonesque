"""
Code in Place 2025 https://codeinplace.stanford.edu/cip5
My notes: https://github.com/egalli64/pythonesque/cip

Makes karel place a diagonal beeper line.
"""

from stanfordkarel import *


def main():
    """
    Put a beeper in each (x, x) cell of the map

    Precondition: Karel is in (1, 1) facing east
    Postcondition: Karel is in the top right cell facing east
    """
    while front_is_clear():
        put_beeper()
        turn_left()
        move()
        turn_right()
        move()
    put_beeper()


def turn_right():
    for i in range(3):
        turn_left()


if __name__ == "__main__":
    """
    Run python from the current directory
    """
    run_karel_program("5x5")
