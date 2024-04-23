"""
Code in Place 2024 https://codeinplace.stanford.edu/cip4
My notes: https://github.com/egalli64/pythonesque/cip

Turn signal: if facing a wall, put down a beeper, turn left, move forward
"""

from stanfordkarel import *


def main():
    if front_is_blocked():
        put_beeper()
        turn_left()
        move()


if __name__ == "__main__":
    """
    Run python from the current directory
    """
    run_karel_program("1x8")
