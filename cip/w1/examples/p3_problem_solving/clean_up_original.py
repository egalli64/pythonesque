"""
Code in Place 2024 https://codeinplace.stanford.edu/cip4
My notes: https://github.com/egalli64/pythonesque/cip

Clean Up Karel: pick any beeper in the current world
"""

from stanfordkarel import *


def main():
    # If we aren't at the top row (we use a while loop because we don't know how many rows there are)
    while left_is_clear():
        ### Pick up a row of beepers ###
        while front_is_clear():
            # Pick up a beeper if present
            if beepers_present():
                pick_beeper()
            move()

        if beepers_present():
            pick_beeper()

        ### Move back to the first column ###
        # Turn around
        for i in range(2):
            turn_left()

        # Move to wall
        while front_is_clear():
            move()

        ### Move up to the next row ###
        # Turn right
        for i in range(3):
            turn_left()
        move()

        ### Reset Karel for loop pre-conditions by turning right to face East ###
        for i in range(3):
            turn_left()

    ### Pick up the final row of beepers ###
    while front_is_clear():
        # Pick up a beeper if present
        if beepers_present():
            pick_beeper()
        move()

    if beepers_present():
        pick_beeper()


if __name__ == "__main__":
    """
    Run python from the current directory, see worlds directory
    """
    run_karel_program("clean_spot")
