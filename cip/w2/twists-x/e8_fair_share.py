"""
Code in Place X 2026 https://codeinplace.stanford.edu/cipx
My notes: https://github.com/egalli64/pythonesque cip folder

Fair Share twist: ask division problems where the answer is always a whole number
"""
from random import randint


def main():
    print("Khansole Academy")

    correct_in_a_row = 0

    while correct_in_a_row < 3:
        num2 = randint(2, 10)  # for division
        true_ans = randint(2, 10)  # for division
        num1 = num2 * true_ans  # for division

        print(f"What is {num1} / {num2}?")  # for division
        user_ans = int(input("Your answer: "))

        if user_ans == true_ans:
            print("Correct!")
            correct_in_a_row += 1
            print(f"You've gotten {correct_in_a_row} correct in a row.")
        else:
            print("Incorrect.")
            correct_in_a_row = 0
            print(f"The expected answer is {true_ans}")
        print()

    print("Congratulations! You mastered division.")  # for division


if __name__ == '__main__':
    main()
