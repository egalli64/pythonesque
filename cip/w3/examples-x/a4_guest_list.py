"""
Code in Place X 2026 https://codeinplace.stanford.edu/cipx
My notes: https://github.com/egalli64/pythonesque cip folder

Guest List: check input against list
"""


def main():
    guests = ["Ana", "Ben", "Cleo"]
    name = input("What is your name? ")

    if name in guests:
        print(f"Welcome, {name}!")
    else:
        guests.append(name)
        print("I've added you on the list:", guests)


if __name__ == "__main__":
    main()
