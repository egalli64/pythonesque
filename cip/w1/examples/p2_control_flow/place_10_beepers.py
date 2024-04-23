"""
Code in Place 2024 https://codeinplace.stanford.edu/cip4
My notes: https://github.com/egalli64/pythonesque/cip

Place 10 beepers (in the current place)
"""

from stanfordkarel import *


def main():
    for i in range(10):
        put_beeper()


if __name__ == "__main__":
    """
    Run python from the current directory
    """
    run_karel_program("1x1")
