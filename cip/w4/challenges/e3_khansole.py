"""
Code in Place 2025 https://codeinplace.stanford.edu/cip5
My notes: https://github.com/egalli64/pythonesque/cip

Week 4: Khansole Academy
--------------------
Randomly generate an addition problem
"""

import random


def main():
    print("Khansole Academy")

    a = random.randrange(10, 100)
    b = random.randrange(10, 100)
    c = str(a + b)
    print(f"What is {a} + {b}?")
    answer = input("Your answer: ")
    if answer == c:
        print("Correct!")
    else:
        print(f"Incorrect.\nThe expected answer is {c}\n")


if __name__ == "__main__":
    main()
