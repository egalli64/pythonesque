"""
Code in Place X 2026 https://codeinplace.stanford.edu/cipx
My notes: https://github.com/egalli64/pythonesque cip folder

Multiplication Tables twist: multiply two random numbers from 2 to 12
"""
from random import randint


def main():
    print("Khansole Academy")

    correct_in_a_row = 0

    while correct_in_a_row < 3:
        num1 = randint(2, 12)  # refactor: new range
        num2 = randint(2, 12)  # refactor: new range

        print(f"What is {num1} * {num2}?")  # refactor: multiply
        user_ans = input("Your answer: ")
        true_ans = str(num1 * num2)  # refactor: multiply

        if user_ans == true_ans:
            print("Correct!")
            correct_in_a_row += 1
            print(f"You've gotten {correct_in_a_row} correct in a row.")
        else:
            print("Incorrect.")
            correct_in_a_row = 0
            print(f"The expected answer is {true_ans}")
        print()

    print("Congratulations! You mastered multiplication.")  # refactor: multiplication


if __name__ == '__main__':
    main()
