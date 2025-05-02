"""
Code in Place 2025 https://codeinplace.stanford.edu/cip5
My notes: https://github.com/egalli64/pythonesque/cip

Dog years: Convert human years to dog years
"""

DOG_YEARS_MULTIPLIER = 7.18


def main():
    years = int(input("Enter an age in calendar years: "))
    dog_years = DOG_YEARS_MULTIPLIER * years
    print("That's", dog_years, "in dog years!")


if __name__ == "__main__":
    main()
