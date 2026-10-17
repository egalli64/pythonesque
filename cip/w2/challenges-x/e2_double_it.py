"""
Code in Place X 2026 https://codeinplace.stanford.edu/cipx
My notes: https://github.com/egalli64/pythonesque cip folder

Program: Double It
--------------------
Ask the user to enter a number
Double that number and print out the result until the value is greater than 100
"""


def main():
    x = int(input("Enter a number: "))
    while x < 100:
        x *= 2
        print(x)


if __name__ == "__main__":
    main()
