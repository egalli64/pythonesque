"""
Code in Place 2024 https://codeinplace.stanford.edu/cip4
My notes: https://github.com/egalli64/pythonesque/cip

Program: Double It
--------------------
Ask the user to enter a number
Double that number and print out the result until the value is greater than 100
"""


def main():
    curr_value = int(input("Enter a number: "))
    while curr_value < 100:
        curr_value *= 2
        print(curr_value)


if __name__ == "__main__":
    main()
