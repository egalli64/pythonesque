"""
Code in Place X 2026 https://codeinplace.stanford.edu/cipx
My notes: https://github.com/egalli64/pythonesque cip folder

Khansole Academy (step 2): Three in a row
"""
from random import randint

WINNING_STRIKE = 3


def main():
    print("Khansole Academy")

    count = 0
    while count < WINNING_STRIKE:
        x = randint(10, 99)
        y = randint(10, 99)

        print(f"What is {x} + {y}?")

        answer = input("Your answer: ")
        result = str(x + y)

        if answer == result:
            count += 1
            print(f"Correct!\nYou've gotten {count} correct in a row.\n")
        else:
            print(f"Incorrect.\nThe expected answer is {result}\n")
            count = 0

    print("Congratulations! You mastered addition.")


if __name__ == "__main__":
    main()
