"""
Memory Puzzle - A simple memory matching game

From: Making Games with Python & Pygame by Al Sweigart - https://inventwithpython.com/pygame/
My reviewed version: https://github.com/egalli64/pythonesque/pygame/makinggames

Step 1b: generate a boolean matrix to keep track of each card visibility
"""

N_ROWS = 4
N_COLS = 2


def build_cards_visibility(x: bool):
    """Build a card visibility matrix (True for visible)"""
    return [[x] * N_COLS for _ in range(N_ROWS)]


if __name__ == "__main__":
    print(build_cards_visibility(True))
    print(build_cards_visibility(False))
