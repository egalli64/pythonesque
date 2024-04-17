"""
Code in Place 2024 https://codeinplace.stanford.edu/cip4
My notes: https://github.com/egalli64/pythonesque/cip

Use of move(), turn_left(), and pick_beeper()
"""

from stanfordkarel import *


def main():
    """
    Karel is initially placed in (2, 4) and directed east, a beeper is place in (5, 3)
    Go, pick the beeper up, and get back home - beware of walls!
    """

    # move east twice
    move()
    move()
    # turn right
    turn_left()
    turn_left()
    turn_left()
    # move south
    move()
    # reach the beeper and pick it up
    turn_left()
    move()
    pick_beeper()
    # turn round
    turn_left()
    turn_left()
    # move west
    move()
    move()
    move()
    # turn right
    turn_left()
    turn_left()
    turn_left()
    # reach the original position
    move()
    turn_left()
    turn_left()
    turn_left()


if __name__ == "__main__":
    """
    Run python from the current directory, see the worlds/warmup.w
    """
    run_karel_program("home")
