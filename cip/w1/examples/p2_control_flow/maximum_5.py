"""
Code in Place 2024 https://codeinplace.stanford.edu/cip4
My notes: https://github.com/egalli64/pythonesque/cip

Maximum 5: Place five beepers on the current row, or less if there is no room enough
"""

from stanfordkarel import *


def main():
    put_beeper()
    for i in range(4):
        if front_is_clear():
            move()
            put_beeper()


if __name__ == "__main__":
    """
    Run python from the current directory
    """
    run_karel_program("8x1")
