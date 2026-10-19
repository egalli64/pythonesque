"""
Code in Place X 2026 https://codeinplace.stanford.edu/cipx
My notes: https://github.com/egalli64/pythonesque cip folder

Story Time twist: ask GPT to turn each problem into a one-sentence story.
"""
from random import randint
from ai import call_gpt  # ChatGPT support

PROMPT = "Convert 'What is {} + {}?' in a one-liner question story."  # for ChatGPT


def main():
    print("Khansole Academy")

    correct_in_a_row = 0

    while correct_in_a_row < 3:
        num1 = randint(10, 99)
        num2 = randint(10, 99)

        problem = call_gpt(PROMPT.format(num1, num2))  # generate a problem
        print(problem)  # let the user know the problem to solve
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
