"""
Code in Place 2024 https://codeinplace.stanford.edu/cip4
My notes: https://github.com/egalli64/pythonesque/cip

Use of move() and pick_beeper()
"""
from stanfordkarel import *


def main():
    # Karel is initially placed in [1, 1] and directed east
    move()
    # Karel is on [2, 1], where a single beeper is placed
    pick_beeper()
    # The beeper has been picked up
    move()
    # Karel is on [3, 1]


if __name__ == '__main__':
    """
    Run python from the current directory, see the worlds/warmup.w
    """
    run_karel_program("warmup")
