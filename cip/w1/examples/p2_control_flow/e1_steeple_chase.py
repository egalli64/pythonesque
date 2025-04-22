"""
Code in Place 2025 https://codeinplace.stanford.edu/cip5
My notes: https://github.com/egalli64/pythonesque/cip

Steeple Chase: walk on the bottom row, but if a wall is met, follow it
"""

from stanfordkarel import *


def main():
    """
    Move or jump hurdle for eight times
    """
    for i in range(8):
        if front_is_clear():
            move()
        else:
            jump_hurdle()


def jump_hurdle():
    """
    Pre-condition:  Facing East at bottom of hurdle
    Post-condition: Facing East at bottom in next avenue after hurdle
    """
    ascend_hurdle()
    move()
    descend_hurdle()


def ascend_hurdle():
    """
    Pre-condition:  Facing East at bottom of hurdle
    Post-condition: Facing East immediately above hurdle
    """
    turn_left()  # Face North

    # While there is a wall on the Eastern side of Karel, move up a row
    while right_is_blocked():
        move()

    turn_right()  # Face East


def descend_hurdle():
    """
    Pre-condition:  Facing East above and immediately after hurdle
    Post-condition: Facing East at bottom of hurdle
    """
    turn_right()  # Face South
    move_to_wall()  # Move to row 1
    turn_left()  # Face East


def move_to_wall():
    """
    Pre-condition:  None
    Post-condition: Facing first wall in whichever direction Karel was facing previously
    """
    while front_is_clear():
        move()


def turn_right():
    """
    Pre-condition:  None
    Post-condition: Karel is facing to the right of whichever direction Karel was facing previously
    """
    for i in range(3):
        turn_left()


if __name__ == "__main__":
    """
    Run python from the current directory
    """
    run_karel_program("steeple_chase")
