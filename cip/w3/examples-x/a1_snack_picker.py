"""
Code in Place X 2026 https://codeinplace.stanford.edu/cipx
My notes: https://github.com/egalli64/pythonesque cip folder

Snack Picker: first, last, random element from a list
"""
import random


def main():
    snacks = ["chips", "popcorn", "grapes", "pretzels", "cookies"]
    print(f"There are {len(snacks)} snacks.")

    print(f"The first snack is {snacks[0]} and the last one is {snacks[- 1]}.")

    pick = random.choice(snacks)
    print("Tonight's snack:", pick)


if __name__ == "__main__":
    main()
