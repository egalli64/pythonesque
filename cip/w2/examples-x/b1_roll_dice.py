"""
Code in Place X 2026 https://codeinplace.stanford.edu/cipx
My notes: https://github.com/egalli64/pythonesque cip folder

Random - Roll Dice
"""
from random import randint

NUM_SIDES = 6


def main():
    die1 = randint(1, NUM_SIDES)
    die2 = randint(1, NUM_SIDES)

    total = die1 + die2

    print("Dice have", NUM_SIDES, "sides each.")
    print("First die:", die1)
    print("Second die:", die2)
    print("Total of two dice:", total)


if __name__ == '__main__':
    main()
