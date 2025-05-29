"""
Code in Place 2025 https://codeinplace.stanford.edu/cip5
My notes: https://github.com/egalli64/pythonesque/cip

Program: Double List
"""


def main():
    numbers = [1, 2, 3, 4]  # Creates a list of numbers

    for i in range(len(numbers)):
        numbers[i] *= 2

    print(numbers)  # This should print the doubled list

if __name__ == "__main__":
    main()
