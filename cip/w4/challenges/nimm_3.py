"""
Code in Place 2024 https://codeinplace.stanford.edu/cip4
My notes: https://github.com/egalli64/pythonesque/cip

Week 4: The Game of Nimm - Milestone 3
--------------------
Ensure just 1 or 2 stones are taken each time
"""


def main():
    stones = 20
    player = 1
    while stones > 0:
        print(f"There are {stones} stones left.")
        taken = 0
        while taken < 1 or taken > 2:
            msg = f"Player {player} Would you like to remove 1 or 2 stones? "
            taken = int(input(msg))
        stones -= taken
        player = 2 if player == 1 else 1

    print("Game over")


if __name__ == "__main__":
    main()
