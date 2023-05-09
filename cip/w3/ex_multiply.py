"""
Code in Place 2023 https://codeinplace.stanford.edu/cip3
My notes: https://github.com/egalli64/pythonesque/cip

Program: multiply two numbers
--------------------
This program asks the user for two
integers and prints the value of the first number
multiplied with the second
"""

def main():
    print("This program multiplies two numbers.")

    first = int(input("Enter first number: "))
    second = int(input("Enter second number: "))

    print(first * second)


if __name__ == '__main__':
    main()