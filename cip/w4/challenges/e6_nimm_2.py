"""
Code in Place 2025 https://codeinplace.stanford.edu/cip5
My notes: https://github.com/egalli64/pythonesque/cip

Week 4: The Game of Nimm - Milestone 2
--------------------
Add a variable to keep track of the current player (1 or 2)
"""


def main():
    stones = 20
    player = 1
    while stones > 0:
        print(f"There are {stones} stones left.")
        taken = int(input(f"Player {player} Would you like to remove 1 or 2 stones? "))
        stones -= taken
        player = 2 if player == 1 else 1

    print("Game over")


if __name__ == "__main__":
    main()
