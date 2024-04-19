"""
Code in Place 2024 https://codeinplace.stanford.edu/cip4
My notes: https://github.com/egalli64/pythonesque/cip

Clean spot: pick any beeper in the current place
"""

from stanfordkarel import *


def main():
    while beepers_present():
        pick_beeper()


if __name__ == "__main__":
    """
    Run python from the current directory
    """
    run_karel_program("clean_spot")
