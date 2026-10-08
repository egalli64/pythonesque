"""
Code in Place X 2026 https://codeinplace.stanford.edu/cipx
My notes: https://github.com/egalli64/pythonesque/cip

Greetings: Ask the user what part of the day it is for them, then greet them accordingly.
"""


def main():
    part = input("Is it morning or night? ")

    if part == "morning":
        print("Good morning!")
    else:
        print("Good evening!")

    print("Have a great day!")


if __name__ == "__main__":
    main()
