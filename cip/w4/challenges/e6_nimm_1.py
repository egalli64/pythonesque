"""
Code in Place 2025 https://codeinplace.stanford.edu/cip5
My notes: https://github.com/egalli64/pythonesque/cip

Week 4: The Game of Nimm - Milestone 1
--------------------
Start with 20 stones. Remove stones and print out how many stones are left until there are zero
"""


def main():
    stones = 20
    while stones > 0:
        print(f"There are {stones} stones left.")
        taken = int(input("Would you like to remove 1 or 2 stones? "))
        stones -= taken

    print("Game over")


if __name__ == "__main__":
    main()
