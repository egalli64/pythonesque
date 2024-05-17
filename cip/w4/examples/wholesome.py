"""
Code in Place 2024 https://codeinplace.stanford.edu/cip4
My notes: https://github.com/egalli64/pythonesque/cip

Wholesome machine: check if the user input the expected sentence
"""

AFFIRMATION = "I am capable of doing anything I put my mind to."


def main():
    print("Please type the following affirmation: " + AFFIRMATION)

    s = input()
    while s != AFFIRMATION:
        print("That was not the affirmation.")

        print("Please type the following affirmation: " + AFFIRMATION)
        s = input()

    print("That's right! :)")


if __name__ == "__main__":
    main()
