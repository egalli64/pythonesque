"""
Code in Place 2025 https://codeinplace.stanford.edu/cip5
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

    for _ in range(3):
        roll_dice()


if __name__ == "__main__":
    main()
