"""
Code in Place Section Leader Application 2024 https://codeinplace.stanford.edu/

My notes: https://github.com/egalli64/pythonesque/cip/karel
"""

from stanfordkarel import *


def main():
    """
    Karel should fill the whole world with beepers

    Loop to fill the current row.
    Before filling the row, check if there is another row,
    if so, after the row is filled move back to square one and then move to the next row
    """
    while front_is_clear():
        if left_is_clear():
            fill_row()
            move_back()
            turn_right()
            move()
            turn_right()
        else:
            fill_row()


def fill_row():
    """
    Fill the current row
    Precondition: Karel is facing east
    Postcondition: Karel is on the last square
    """
    put_beeper()
    while front_is_clear():
        move()
        put_beeper()


def move_back():
    """
    Move back to square one on the current row
    Precondition: Karel is facing east
    Postcondition: Karel is on square one, facing west
    """
    turn_back()
    while front_is_clear():
        move()


def turn_back():
    """
    Utility function, prepare Karel to move to the opposite direction
    """
    turn_left()
    turn_left()


def turn_right():
    """
    Utility function, turn Karel right
    """
    turn_left()
    turn_left()
    turn_left()


# There is no need to edit code beyond this point
if __name__ == "__main__":
    run_karel_program()
