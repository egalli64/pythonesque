"""
Code in Place X 2026 https://codeinplace.stanford.edu/cipx
My notes: https://github.com/egalli64/pythonesque/cip

Secret Word: Keep asking for a secret word until the user types it correctly.
"""
SECRET = "sunrise"


def main():
    while True:
        tentative = input("Type the secret word: ")
        if tentative == SECRET:
            print("Ready!")
            break
        else:
            print("Try again!")


if __name__ == "__main__":
    main()
