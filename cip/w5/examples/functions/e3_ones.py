"""
Code in Place 2025 https://codeinplace.stanford.edu/cip5
My notes: https://github.com/egalli64/pythonesque/cip

Print ones digit
define a function print_ones_digit that prints just the units of the passed number
"""


def main():
    num = int(input("Enter a number: "))
    print_ones_digit(num)


def print_ones_digit(num):
    print("The ones digit is", num % 10)


if __name__ == "__main__":
    main()
