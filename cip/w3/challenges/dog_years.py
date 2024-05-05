"""
Code in Place 2024 https://codeinplace.stanford.edu/cip4
My notes: https://github.com/egalli64/pythonesque/cip

Dog years: Convert human years to dog years
"""

DOG_YRS_MULTIPLIER = 7.18


def main():
    years = int(input("Enter an age in calendar years: "))
    dog_years = DOG_YRS_MULTIPLIER * years
    print("That's", dog_years, "in dog years!")


if __name__ == "__main__":
    main()
