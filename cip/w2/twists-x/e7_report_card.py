"""
Code in Place X 2026 https://codeinplace.stanford.edu/cipx
My notes: https://github.com/egalli64/pythonesque cip folder

Report Card twist: add a final recap
"""
from random import randint


def main():
    print("Khansole Academy")

    correct_in_a_row = 0
    total_count = 0  # for report card

    while correct_in_a_row < 3:
        num1 = randint(10, 99)
        num2 = randint(10, 99)

        print(f"What is {num1} + {num2}?")
        user_ans = int(input("Your answer: "))
        true_ans = num1 + num2

        total_count += 1  # for report card
        if user_ans == true_ans:
            print("Correct!")
            correct_in_a_row += 1
            print(f"You've gotten {correct_in_a_row} correct in a row.")
        else:
            print("Incorrect.")
            correct_in_a_row = 0
            print(f"The expected answer is {true_ans}")
        print()

    print("Congratulations! You mastered addition.")
    print(f"You tried {total_count} problems and got {correct_in_a_row} right.")  # report card


if __name__ == '__main__':
    main()
