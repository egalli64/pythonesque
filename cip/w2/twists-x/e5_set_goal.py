"""
Code in Place X 2026 https://codeinplace.stanford.edu/cipx
My notes: https://github.com/egalli64/pythonesque cip folder

Set the Goal twist
"""
from random import randint


def main():
    print("Khansole Academy")

    goal = int(input("How many in a row do you want to get? "))  # ask the goal to user
    correct_in_a_row = 0

    while correct_in_a_row < goal:  # use the custom goal
        num1 = randint(10, 99)
        num2 = randint(10, 99)

        print(f"What is {num1} + {num2}?")
        user_ans = int(input("Your answer: "))
        true_ans = num1 + num2

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


if __name__ == '__main__':
    main()
