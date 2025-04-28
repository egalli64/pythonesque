"""
Code in Place 2025 https://codeinplace.stanford.edu/cip5
My notes: https://github.com/egalli64/pythonesque/cip

Move 5: move forward five times
"""

from stanfordkarel import *


def main():
    for i in range(5):
        move()


if __name__ == "__main__":
    """
    Run python from the current directory
    """
    run_karel_program("6x5")
