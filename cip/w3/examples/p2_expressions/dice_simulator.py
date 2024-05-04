"""
Code in Place 2024 https://codeinplace.stanford.edu/cip4
My notes: https://github.com/egalli64/pythonesque/cip

Dice simulator: Simulate rolling two dice, three times
"""

import random

NUM_SIDES = 6


def roll_dice():
    """
    Simulates rolling two dice and prints their total
    """
    total = random.randint(1, NUM_SIDES) + random.randint(1, NUM_SIDES)
    print("Total of two dice:", total)


def main():
    # random.seed(1)

    roll_dice()
    roll_dice()
    roll_dice()


if __name__ == "__main__":
    main()
