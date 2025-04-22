"""
Code in Place 2025 https://codeinplace.stanford.edu/cip5
My notes: https://github.com/egalli64/pythonesque/cip

Move Beeper: remove the beeper in (2, 1) and add one in (2, 3)
"""

from stanfordkarel import *


def main():
    """
    Precondition: Karel is in (1, 1) and directed East
    Postcondition: Karel is in (3, 3) and directed East
    """
    move()
    pick_beeper()
    go_target()
    put_beeper()
    move()


def go_target():
    """
    Precondition: Karel has just removed the beeper, and is directed East
    Postcondition: Karel is ready to put the beeper, and is directed East
    """
    turn_left()
    move()
    move()
    for i in range(3):
        turn_left()


if __name__ == "__main__":
    """
    Run python from the current directory, see the worlds folder
    """
    run_karel_program("movebeeper")
