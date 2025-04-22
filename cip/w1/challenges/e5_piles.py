"""
Code in Place 2025 https://codeinplace.stanford.edu/cip5
My notes: https://github.com/egalli64/pythonesque/cip

Piles: pick up all the beepers on the first row of this world
"""

from stanfordkarel import *


def main():
    """
    Precondition: Karel is in (1, 1), facing East, three piles of ten beepers are in the assigned places
    Postcondition: Karel is in (7, 1), facing East, no more beepers
    """
    move()
    # In (2, 1)
    pick_10_beepers()

    move()
    move()
    # In (4, 1)
    pick_10_beepers()

    move()
    move()
    # In (6, 1)
    pick_10_beepers()

    move()


def pick_10_beepers():
    """
    Precondition: 10 beepers are in the current place
    Postcondition: no more beepers
    """
    for i in range(10):
        pick_beeper()


if __name__ == "__main__":
    """
    Run python from the current directory, see the worlds/warmup.w
    """
    run_karel_program("piles")
