"""
Code in Place 2025 https://codeinplace.stanford.edu/cip5
My notes: https://github.com/egalli64/pythonesque/cip

Program: Add Many Numbers
"""


def add_many_numbers(numbers):
    """
    Takes in a list of numbers and returns the sum of those numbers.
    """
    result = 0

    for number in numbers:
        result += number

    return result


def main():
    numbers = [1, 2, 3, 4, 5]  # Make a list of numbers
    sum_of_numbers = add_many_numbers(numbers)  # Find the sum of the list
    print(sum_of_numbers)  # Print out the sum above


if __name__ == "__main__":
    main()
