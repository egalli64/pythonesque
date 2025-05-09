"""
Code in Place 2025 https://codeinplace.stanford.edu/cip5
My notes: https://github.com/egalli64/pythonesque/cip

Week 4: The Game of Nimm - Milestone 4
--------------------
Announce the winner
"""


def main():
    stones = 20
    player = 1
    while stones > 0:
        print(f"There are {stones} stones left.")
        taken = int(input(f"Player {player} would you like to remove 1 or 2 stones? "))
        while taken < 1 or taken > 2:
            taken = int(input("Please enter 1 or 2: "))
        stones -= taken
        player = 2 if player == 1 else 1
        print()

    print(f"Player {player} wins!")


if __name__ == "__main__":
    main()
