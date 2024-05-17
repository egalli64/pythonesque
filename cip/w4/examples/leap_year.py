"""
Code in Place 2024 https://codeinplace.stanford.edu/cip4
My notes: https://github.com/egalli64/pythonesque/cip

Leap year: divisible by 4, but not divisible by 100, unless divisible by 400
"""

import calendar


def main():
    year = int(input("Please input a year: "))

    # 1. step by step
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("That's a leap year!")
            else:
                print("That's not a leap year.")
        else:
            print("That's a leap year!")
    else:
        print("That's not a leap year.")

    # 2. compressed rule
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print("That's a leap year!")
    else:
        print("That's not a leap year.")

    # 3. standard library
    if calendar.isleap(year):
        print("That's a leap year!")
    else:
        print("That's not a leap year.")


if __name__ == "__main__":
    main()
