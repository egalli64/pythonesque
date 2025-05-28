"""
Code in Place 2025 https://codeinplace.stanford.edu/cip5
My notes: https://github.com/egalli64/pythonesque/cip

Worked example: Is Odd
"""


def main():
    for i in range(10):
        if is_odd(i):
            print("odd")
        else:
            print("even")


def is_odd(value):
    """
    Checks to see if a value is odd. If it is, returns true.
    """

    remainder = value % 2  # 0 if value is divisible by 2, 1 if it isn't
    return remainder == 1


if __name__ == "__main__":
    main()
