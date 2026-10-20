"""
Code in Place X 2026 https://codeinplace.stanford.edu/cipx
My notes: https://github.com/egalli64/pythonesque cip folder

Plus or Minus twist: randomly ask for addition or subtraction.
"""
from random import randint


def main():
    print("Khansole Academy")

    correct_in_a_row = 0

    while correct_in_a_row < 3:
        num1 = randint(10, 99)
        num2 = randint(10, 99)

        # begin +/- fix
        if randint(0, 1):
            sign = "+"
            true_ans = num1 + num2
        else:
            sign = "-"
            true_ans = num1 - num2
        print(f"What is {num1} {sign} {num2}?")
        # end +/- fix

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

    print("Congratulations! You mastered addition/subtraction.")  # +/- fix


if __name__ == "__main__":
    main()
