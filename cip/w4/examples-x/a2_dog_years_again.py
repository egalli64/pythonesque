"""
Code in Place X 2026 https://codeinplace.stanford.edu/cipx
My notes: https://github.com/egalli64/pythonesque cip folder

Dog Years, Again
"""


def dog_years(age):
    return age * 7


def main():
    age = int(input("How old are you? "))
    print(f"You are {dog_years(age)} in dog years.")
    print(f"Next year you will be {dog_years(age + 1)}.")


if __name__ == "__main__":
    main()
