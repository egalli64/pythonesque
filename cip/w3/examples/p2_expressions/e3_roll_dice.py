"""
Code in Place 2025 https://codeinplace.stanford.edu/cip5
My notes: https://github.com/egalli64/pythonesque/cip

Roll Dice: roll two dice, print each roll and the total
"""

import random

NUM_SIDES = 6


def main():
    # random.seed(1)

    first = random.randint(1, NUM_SIDES)
    second = random.randint(1, NUM_SIDES)

    total = first + second

    print("Dice have", NUM_SIDES, "sides each.")
    print("First die:", first)
    print("Second die:", second)
    print("Total of two dice:", total)


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == "__main__":
    main()
