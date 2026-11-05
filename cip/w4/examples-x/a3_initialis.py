"""
Code in Place X 2026 https://codeinplace.stanford.edu/cipx
My notes: https://github.com/egalli64/pythonesque cip folder

Initials
"""


def initial(name):
    return name[0].upper()


def main():
    initials = initial(input("First name: "))
    initials += initial(input("Middle name: "))
    initials += initial(input("Last name: "))

    print("Your initials:", initials)


if __name__ == "__main__":
    main()
