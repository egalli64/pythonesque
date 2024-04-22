"""
Code in Place 2024 https://codeinplace.stanford.edu/cip4
My notes: https://github.com/egalli64/pythonesque/cip

Fill bottom row
"""

from stanfordkarel import *


def main():
    put_beeper()
    while front_is_clear():
        move()
        put_beeper()


if __name__ == "__main__":
    """
    Run python from the current directory
    """
    run_karel_program("8x1")
