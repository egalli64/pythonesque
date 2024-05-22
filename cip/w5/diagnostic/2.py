"""
Code in Place 2023 https://codeinplace.stanford.edu/cip3
My notes: https://github.com/egalli64/pythonesque/cip

Diagnostic 2

Print out each of the numbers 1 through 100 and whether that number is even or odd.
"""
# print numbers from 1 up until MAX_NUMBER, inclusive
MAX_NUMBER = 100


def main():
    for i in range(1, MAX_NUMBER + 1):
        print(i, "is", "odd" if i % 2 == 1 else "even")


if __name__ == "__main__":
    main()
