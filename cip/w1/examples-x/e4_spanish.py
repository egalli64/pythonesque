"""
Code in Place X 2026 https://codeinplace.stanford.edu/cipx
My notes: https://github.com/egalli64/pythonesque/cip

Spanish Quiz: Quiz the user on one Spanish word, using != to check their answer.
"""


def main():
    word = input("How do you say Hello in Spanish? ")

    if word != "Hola":
        print("That is incorrect.")
    else:
        print("This is correct!")


if __name__ == "__main__":
    main()
