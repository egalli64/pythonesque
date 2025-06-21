"""
Code in Place 2025 https://codeinplace.stanford.edu/cip5
My notes: https://github.com/egalli64/pythonesque/cip

Week 4: Khansole Academy
--------------------
Spot the bug
"""

import random


def main():
    print("Khansole Academy")

    first_rand_num = random.randint(10, 100)
    second_rand_num = random.randint(10, 100)
    correct_answer = first_rand_num + second_rand_num

    print(f"What is {first_rand_num} + {second_rand_num}?")
    user_input = int(input("Your answer: "))
    if user_input == correct_answer:
        print("Correct!")
    else:
        print("Incorrect.")
        print(f"The expected answer is {correct_answer}")


if __name__ == "__main__":
    main()
