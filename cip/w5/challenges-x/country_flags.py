"""
Code in Place X 2026 https://codeinplace.stanford.edu/cipx
My notes: https://github.com/egalli64/pythonesque cip folder

Country Flags
"""
from flags import build_flag_dictionary


def main():
    flags = build_flag_dictionary()
    country = input("What country are you from? ")

    key = country.lower()
    if key in flags:
        print("Here is your flag:", flags[key])
        print(f"Welcome to Code in Place X, friend from {country}!")
    else:
        print("Sorry, that country is not in the dictionary. Maybe try a different spelling!")


if __name__ == "__main__":
    main()
