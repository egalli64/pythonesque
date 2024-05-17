"""
Code in Place 2024 https://codeinplace.stanford.edu/cip4
My notes: https://github.com/egalli64/pythonesque/cip

Guess My Number
"""

import random

SOLUTION = random.randint(1, 99)


def main():
    print("I am thinking of a number between 1 and 99...")
    guess = int(input("Enter a guess: "))

    while guess != SOLUTION:
        print("Your guess is too ", end="")
        print("low" if guess < SOLUTION else "high")
        print()
        guess = int(input("Enter a new guess: "))

    print(f"Congrats! The number was: {SOLUTION}")


if __name__ == "__main__":
    main()
