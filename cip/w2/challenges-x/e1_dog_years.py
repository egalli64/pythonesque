"""
Code in Place X 2026 https://codeinplace.stanford.edu/cipx
My notes: https://github.com/egalli64/pythonesque cip folder

Dog years: Convert human years to dog years
"""
# Each year for a human is like 7.18 years for a dog
DOG_YRS_MULTIPLIER = 7.18


def main():
    age = int(input("Enter an age in calendar years: "))
    dog_age = age * DOG_YRS_MULTIPLIER
    print(f"That's {dog_age} in dog years!")


if __name__ == "__main__":
    main()
