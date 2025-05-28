"""
Code in Place 2025 https://codeinplace.stanford.edu/cip5
My notes: https://github.com/egalli64/pythonesque/cip

Program: Memory Game
"""

import random

NUM_PAIRS = 3
NUM_ITEMS = NUM_PAIRS * 2


def main():
    # M1. Create the truth list, with pairs of equal values in [0 .. NUM_PAIRS)
    truth = []
    for i in range(NUM_PAIRS):
        truth.append(i)
        truth.append(i)

    # M2. Shuffle the list
    random.shuffle(truth)

    # M3. Create a displayed list, initialized with all '*'
    displayed = []

    for i in range(NUM_ITEMS):
        displayed.append("*")

    # extra: keeping track of the revealed indices makes the algorithm simpler
    revealed_indices = set()

    # M6. Play multiple turns (part 1 - loop)
    while len(revealed_indices) < NUM_ITEMS:
        # M4. Get two valid indices from the user
        print(displayed)

        i = get_index(revealed_indices, -1)
        j = get_index(revealed_indices, i)

        # M5. Check correct
        if truth[i] == truth[j]:
            displayed[i] = truth[i]
            displayed[j] = truth[j]
            revealed_indices.add(i)
            revealed_indices.add(j)
            print("Match!")
        else:
            print(f"Value at index {i} is {truth[i]}")
            print(f"Value at index {j} is {truth[j]}")
            print("No match. Try again.")
            input("Press Enter to continue...")

        # M6. Part 2
        clear_terminal()

    # M6. Part 3
    print(displayed)
    print("Congratulations! You won!")


def get_index(revealed_indices, previous):
    """see M4"""
    while True:
        buffer = input("Enter an index: ")
        index = -1
        try:
            index = int(buffer)
        except:
            print("Not a number. Try again.")

        if index < 0 or index >= NUM_ITEMS:
            print("Invalid index. Try again.")
        elif index == previous:
            print("You entered the same index twice. Try again.")
        elif index in revealed_indices:
            print("This number has already been matched. Try again.")
        else:
            return index


def clear_terminal():
    for i in range(20):
        print("\n")


if __name__ == "__main__":
    main()
