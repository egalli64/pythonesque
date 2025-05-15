"""
Code in Place 2025 https://codeinplace.stanford.edu/cip5
My notes: https://github.com/egalli64/pythonesque/cip

Program: High-Low Game

1. Two numbers are generated in [1 .. 100], one for you and one for a computer. You see only your number
2. You make a guess, saying your number is either higher or lower than the computer's one
3. If you get it, you get a point

The game is in a given number of rounds

Extra requirements
"""

import random

NUM_ROUNDS = 5


def main():
    print("Welcome to the High-Low Game!")
    print("--------------------------------")

    # M5: keep track of the player score
    score = 0

    # M4: multiple rounds
    for i in range(NUM_ROUNDS):
        print("Round", i + 1)
        # M1: random numbers generation and printing
        computer = random.randint(1, 100)
        player = random.randint(1, 100)
        print("Your number is", player)

        # M2: player choice
        s = input("Do you think your number is higher or lower than the computer's?: ")

        # X1: check for valid choice
        while s != "higher" and s != "lower":
            s = input("Please enter either higher or lower: ")

        # M3: check the guess
        if s == "higher" and player > computer or s == "lower" and player < computer:
            print("You were right! The computer's number was", computer)
            # M5: keep track of the player score
            score += 1
        else:
            print("Aww, that's incorrect. The computer's number was", computer)

        # M5: keep track of the player score
        print(f"Your score is now {score}\n")

    print("Your final score is", score)

    # X2: Conditional ending messages based on performance
    if score == NUM_ROUNDS:
        print("Wow! You played perfectly!")
    elif score > NUM_ROUNDS // 2:
        print("Good job, you played really well!")
    else:
        print("Better luck next time!")


if __name__ == "__main__":
    main()
