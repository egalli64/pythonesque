"""
Code in Place X 2026 https://codeinplace.stanford.edu/cipx
My notes: https://github.com/egalli64/pythonesque/cip

Wholesome Machine: Write a program which prompts the user to type the required affirmation correctly.
"""
SOLUTION = "I can do anything I put my mind to."


def main():
    while True:
        print("Please type the following affirmation:", SOLUTION)
        affirmation = input()
        if affirmation == SOLUTION:
            print("That's right! :)")
            break
        else:
            print("That was not the affirmation.")


if __name__ == "__main__":
    main()
