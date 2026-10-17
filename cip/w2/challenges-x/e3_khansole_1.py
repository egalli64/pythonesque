"""
Code in Place X 2026 https://codeinplace.stanford.edu/cipx
My notes: https://github.com/egalli64/pythonesque cip folder

Khansole Academy (step 1): Randomly generate an addition problem
"""
from random import randint


def main():
    print("Khansole Academy")

    x = randint(10, 99)
    y = randint(10, 99)

    print(f"What is {x} + {y}?")

    result = str(x + y)
    answer = input("Your answer: ")

    if answer == result:
        print("Correct!")
    else:
        print(f"Incorrect.\nThe expected answer is {result}\n")


if __name__ == "__main__":
    main()
