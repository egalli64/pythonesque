"""
Code in Place 2024 https://codeinplace.stanford.edu/cip4
My notes: https://github.com/egalli64/pythonesque/cip

Rainbow: paint the first cells in the current row in Red, Orange, Yellow, Green, and Blue
Use the paint_corner() function
"""

from stanfordkarel import *


def main():
    """
    Precondition: Karel is in (1, 1) facing East
    Postcondition: Karel is in (6, 1) facing East
    """
    paint_corner('Red')
    move()
    paint_corner('Orange')
    move()
    paint_corner('Yellow')
    move()
    paint_corner('Green')
    move()
    paint_corner('Blue')
    move()


if __name__ == "__main__":
    """
    Run python from the current directory
    """
    run_karel_program("8x1")
