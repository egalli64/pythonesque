"""
Code in Place 2024 https://codeinplace.stanford.edu/cip4
My notes: https://github.com/egalli64/pythonesque/cip

Use of move() and pick_beeper() to pick up all the beepers on the first row of this world
"""

from stanfordkarel import *


def main():
    # Karel is initially placed in (1, 1) and directed east, and should end up in (7, 1)
    move()
    # Now Karel is in (2, 1), pick the ten beeper
    for i in range(10):
        pick_beeper()

    move()
    move()
    # Karel is on (4, 1)
    for i in range(10):
        pick_beeper()

    move()
    move()
    # Karel is on (6, 1)
    for i in range(10):
        pick_beeper()

    move()

if __name__ == "__main__":
    """
    Run python from the current directory, see the worlds/warmup.w
    """
    run_karel_program("piles")
