"""
Code in Place 2024 https://codeinplace.stanford.edu/cip4
My notes: https://github.com/egalli64/pythonesque/cip

International voting age: check the input against some defined voting ages
"""

PETURKSBOUIPO_AGE = 16
STANLAU_AGE = 25
MAYENGUA_AGE = 48


def print_vote_info(place, age):
    print(f" vote in {place} where the voting age is {age}.")


def main():
    age = int(input("How old are you? "))

    print("You can", end="")
    if age < PETURKSBOUIPO_AGE:
        print("not", end="")
    print_vote_info("Peturksbouipo", PETURKSBOUIPO_AGE)

    print("You can", end="")
    if age < STANLAU_AGE:
        print("not", end="")
    print_vote_info("Stanlau", STANLAU_AGE)

    print("You can", end="")
    if age < MAYENGUA_AGE:
        print("not", end="")
    print_vote_info("Mayengua", MAYENGUA_AGE)


if __name__ == "__main__":
    main()
