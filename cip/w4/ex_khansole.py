"""
Code in Place 2023 https://codeinplace.stanford.edu/cip3
My notes: https://github.com/egalli64/pythonesque/cip

Week 4: Khansole Academy - Three in a row
--------------------
Randomly generate addition problems until the user has gotten 3 problems correct in a row
"""
import random

WINNING_STRIKE = 3

def main():
    print("Khansole Academy")

    i = 0
    while i < WINNING_STRIKE:
        a = random.randrange(10, 100)
        b = random.randrange(10, 100)
        c = str(a + b)
        print(f"What is {a} + {b}?")
        answer = input("Your answer: ")
        if answer == c:
            i += 1
            print(f"Correct! You've gotten {i} correct in a row.")
        else:
            print(f"Incorrect. The expected answer is {c}")
            i = 0

    print("Congratulations! You mastered addition.")


if __name__ == '__main__':
    main()
