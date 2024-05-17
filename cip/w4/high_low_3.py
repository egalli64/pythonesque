"""
Code in Place 2024 https://codeinplace.stanford.edu/cip4
My notes: https://github.com/egalli64/pythonesque/cip

Program: High-Low Game

1. Two numbers are generated in [1 .. 100], one for you and one for a computer. You see only your number
2. You make a guess, saying your number is either higher or lower than the computer's one
3. If you get it, you get a point

The game is in a given number of rounds

Milestone #3: The game logic
"""

import random

NUM_ROUNDS = 5


def main():
    print("Welcome to the High-Low Game!")
    print("--------------------------------")

    # 1
    user = random.randint(1, 100)
    computer = random.randint(1, 100)

    print("The computer's number is", computer)
    print("Your number is", user)

    # 2
    s = input("Do you think your number is higher or lower than the computer's?: ")

    # 3
    if s == "higher" and user > computer or s == "lower" and user < computer:
        print("You were right! The computer's number was", computer)
    else:
        print("Aww, that's incorrect. The computer's number was", computer)


if __name__ == "__main__":
    main()
