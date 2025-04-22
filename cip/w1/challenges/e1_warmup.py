"""
Code in Place 2025 https://codeinplace.stanford.edu/cip5
My notes: https://github.com/egalli64/pythonesque/cip

Warmup: Pick the beeper up, then move
"""

from stanfordkarel import *


def main():
    """
    Precondition: Karel is in (1, 1), facing East, there is a beeper in (2, 1)
    Postcondition: Karel is in (3, 1), facing East
    """
    move()
    # now Karel is on (2, 1)
    pick_beeper()
    # The beeper has been picked up
    move()


if __name__ == "__main__":
    """
    Run python from the current directory, see the worlds/warmup.w
    """
    run_karel_program("warmup")
