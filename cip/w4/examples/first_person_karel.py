"""
Code in Place 2024 https://codeinplace.stanford.edu/cip4
My notes: https://github.com/egalli64/pythonesque/cip

First person Karel: Play Karel in a rectangular world
 Implement move and turn left commands
 Store the number of columns and rows in the world as constants
 Start in (1, 1) facing East
 Ask the user for command (Enter to terminate)
 Do not allow the user to crash against the end of the world
"""

N_COLS = 3
N_ROWS = 3

P = "What would you like to do? You can move and turn left. Press enter to finish. "


def print_position_forward(row, col):
    print("You moved one step forward and ", end="")
    print(f"now you're at row {row} column {col}.")


def main():
    direction = "East"
    row = 1
    col = 1

    print("Welcome to first person Karel! ", end="")
    print(f"You're at row {row}, column {col}, ", end="")
    print(f"facing {direction} (facing column {N_COLS})")

    command = input(P)
    while command != "":
        if command == "move":
            if direction == "East" and col < N_COLS:
                col += 1
                print_position_forward(row, col)
            elif direction == "West" and col > 1:
                col -= 1
                print_position_forward(row, col)
            elif direction == "North" and row < N_ROWS:
                row += 1
                print_position_forward(row, col)
            elif direction == "South" and row > 1:
                row -= 1
                print_position_forward(row, col)
            else:
                print("You can't move forward!")
        elif command == "turn left":
            if direction == "East":
                direction = "North"
            elif direction == "North":
                direction = "West"
            elif direction == "West":
                direction = "South"
            elif direction == "South":
                direction = "East"
            print(f"You turned left and are now facing {direction}.")

        command = input(P)

    print(f"You've ended up at row {row} and column {col} facing {direction}.")


if __name__ == "__main__":
    main()
