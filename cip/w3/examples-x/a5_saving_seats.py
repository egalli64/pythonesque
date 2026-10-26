"""
Code in Place X 2026 https://codeinplace.stanford.edu/cipx
My notes: https://github.com/egalli64/pythonesque cip folder

Saving Seats: changing elements in a list
"""


def main():
    seats = ["open", "Ana", "open", "open", "open"]
    print("Seats:", seats)

    name = input("What is your name? ")
    i = int(input("Pick a seat from 0 to 4: "))

    if 0 <= i <= 4:
        if seats[i] == "open":
            seats[i] = name
            print("Done,", name)
        else:
            print(f"Sorry, {seats[i]} is already in that seat.")
    else:
        print("Sorry, bad seat.")

    print("Seats:", seats)


if __name__ == "__main__":
    main()
