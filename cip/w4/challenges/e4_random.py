"""
Code in Place 2025 https://codeinplace.stanford.edu/cip5
My notes: https://github.com/egalli64/pythonesque/cip

Program: Random Numbers
--------------------
Print out ten random numbers in the range 1 to 100, inclusive.
"""

import random


def main():
    for i in range(10):
        value = random.randint(1, 100)
        print(value)


if __name__ == "__main__":
    main()
