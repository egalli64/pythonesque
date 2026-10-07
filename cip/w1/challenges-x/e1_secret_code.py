"""
Code in Place X 2026 https://codeinplace.stanford.edu/cipx
My notes: https://github.com/egalli64/pythonesque/cip

Secret Code: Write a program that asks the user to enter the secret code to unlock a treasure chest.
"""
SOLUTION = "unicorn"


def main():
    secret = input("Enter the secret code: ")
    if secret == SOLUTION:
        print("The treasure chest opens!")
    else:
        print("Access denied! The treasure stays locked.")


if __name__ == "__main__":
    main()
