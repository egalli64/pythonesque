"""
Code in Place 2025 https://codeinplace.stanford.edu/cip5
My notes: https://github.com/egalli64/pythonesque/cip

Program: High-Low Game

1. Two numbers are generated in [1 .. 100], one for you and one for a computer. You see only your number
2. You make a guess, saying your number is either higher or lower than the computer's one
3. If you get it, you get a point

The game is in a given number of rounds

Ready for submission
"""

import random

NUM_ROUNDS = 5


def main():
    print("Welcome to the High-Low Game!")
    print("--------------------------------")

    score = 0
    for i in range(NUM_ROUNDS):
        print("Round", i + 1)
        computer = random.randint(1, 100)
        player = random.randint(1, 100)
        print("Your number is", player)

        s = input("Do you think your number is higher or lower than the computer's?: ")
        if s == "higher" and player > computer or s == "lower" and player < computer:
            print("You were right! The computer's number was", computer)
            score += 1
        else:
            print("Aww, that's incorrect. The computer's number was", computer)

        print(f"Your score is now {score}\n")

    print("Thanks for playing!")


if __name__ == "__main__":
    main()
