"""
Code in Place 2025 https://codeinplace.stanford.edu/cip5
My notes: https://github.com/egalli64/pythonesque/cip

Khansole Academy (step 1): Randomly generate an addition problem
"""
import random


def main():
    print("Khansole Academy")

    x = random.randint(10, 99)
    y = random.randint(10, 99)

    print(f"What is {x} + {y}?")

    result = str(x + y)
    answer = input("Your answer: ")

    if answer == result:
        print("Correct!")
    else:
        print(f"Incorrect.\nThe expected answer is {result}\n")


if __name__ == "__main__":
    main()
