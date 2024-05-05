"""
Code in Place 2024 https://codeinplace.stanford.edu/cip4
My notes: https://github.com/egalli64/pythonesque/cip

Weighted coin: flip a coin having 70% head probability and print the outcome
"""

import random

HEADS = 0.7


def main():
    print("Heads!" if random.random() < HEADS else "Tails!")


if __name__ == "__main__":
    main()
