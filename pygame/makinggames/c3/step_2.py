"""
Memory Puzzle - A simple memory matching game

From: Making Games with Python & Pygame by Al Sweigart - https://inventwithpython.com/pygame/

Step 2: generate a boolean list to keep track of cards visibility
"""

# the board is structured in a even number of squared boxes with gaps between boxes
N_COLS = 2
N_ROWS = 4
assert (N_COLS * N_ROWS) % 2 == 0, "Even number of boxes expected"


def build_cards_visibility(x: bool):
    """
    Build a col-row list for the cards visibility

    Notice that, following the original code, the resulting order is inverted:
    given N_COLS = 2 and N_ROWS = 4, a list with 2 lines of 4 items is returned
    """
    return [[x] * N_ROWS for _ in range(N_COLS)]


if __name__ == "__main__":
    print(build_cards_visibility(True))
    print(build_cards_visibility(False))
