"""
Code in Place 2024 https://codeinplace.stanford.edu/cip4
My notes: https://github.com/egalli64/pythonesque/cip

Remainder division: given the dividend and divisor, calculate quotient and remainder
"""


def main():
    dividend = int(input("Please enter an integer to be divided: "))
    divisor = int(input("Please enter an integer to divide by: "))

    quotient = dividend // divisor
    remainder = dividend % divisor

    print("The result of this division is", quotient, "with a remainder of", remainder)


# There is no need to edit code beyond this point

if __name__ == "__main__":
    main()
