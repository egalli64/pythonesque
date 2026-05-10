"""
Memory Puzzle - A simple memory matching game

From: Making Games with Python & Pygame by Al Sweigart - https://inventwithpython.com/pygame/

Step 1: generate the board, with couples of cards with random shape/color
"""

import random

# the board is structured in a even number of squared boxes with gaps between boxes
N_COLS = 2
N_ROWS = 4
assert (N_COLS * N_ROWS) % 2 == 0, "Even number of boxes expected"


# colors - RGB format
GRAY = (100, 100, 100)
NAVYBLUE = (60, 60, 100)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 128, 0)
PURPLE = (255, 0, 255)
CYAN = (0, 255, 255)
COLORS = (RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE, CYAN)

# shapes - what the player sees
DONUT = "donut"
SQUARE = "square"
DIAMOND = "diamond"
LINES = "lines"
OVAL = "oval"
SHAPES = (DONUT, SQUARE, DIAMOND, LINES, OVAL)


def get_board():
    """
    A col-row list that could contain any possible shape in any possible color

    Notice that, following the original code, the board is inverted: column-rows
    """

    # list of tuples with any possible color/shape combination
    items = []
    for color in COLORS:
        for shape in SHAPES:
            items.append((shape, color))

    # shuffled
    random.shuffle(items)

    # take just the required ones
    count = N_COLS * N_ROWS // 2
    items = items[:count] * 2
    random.shuffle(items)

    return [items[i : i + N_ROWS] for i in range(0, len(items), N_ROWS)]


if __name__ == "__main__":
    print(get_board())
