"""
Code in Place 2025 https://codeinplace.stanford.edu/cip5
My notes: https://github.com/egalli64/pythonesque/cip

Square: place 4 beepers in a 2x2 square
"""

from stanfordkarel import *


def main():
    while no_beepers_present():
        put_beeper()
        move()
        turn_left()


if __name__ == "__main__":
    """
    Run python from the current directory
    """
    run_karel_program("2x2")
