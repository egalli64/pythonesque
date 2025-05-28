"""
Code in Place 2025 https://codeinplace.stanford.edu/cip5
My notes: https://github.com/egalli64/pythonesque/cip

Program: Compute Average

Compute the average of the values in the file and print it
"""

FILE_NAME = "cip/w6/challenges/e1_numbers.txt"


def main():
    number_list = load_numbers_from_file(FILE_NAME)
    sum = 0
    for number in number_list:
        sum += number
    print("Average:", sum / len(number_list))


def load_numbers_from_file(filepath):
    """
    Loads numbers from a file into a list and returns it.
    We assume the file to have one number per line.
    Returns a list of numbers. You should not modify this
    function.
    """
    numbers = []
    with open(filepath, "r") as file_reader:
        for line in file_reader.readlines():
            cleaned_line = line.strip()
            if cleaned_line != "":
                numbers.append(float(cleaned_line))

    return numbers


if __name__ == "__main__":
    main()
