"""
Code in Place 2024 https://codeinplace.stanford.edu/cip4
My notes: https://github.com/egalli64/pythonesque/cip

n-sided dice: Get the number of sides, roll the dice
"""

import random


def main():
    sides = int(input("How many sides does your dice have? "))
    roll = random.randint(1, sides)
    print("Your roll is", roll)


if __name__ == "__main__":
    main()
