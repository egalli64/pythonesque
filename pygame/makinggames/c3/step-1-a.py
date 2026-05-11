"""
Memory Puzzle - A simple memory matching game

From: Making Games with Python & Pygame by Al Sweigart - https://inventwithpython.com/pygame/
My reviewed version: https://github.com/egalli64/pythonesque/pygame/makinggames

Step 1a: generate the board, with couples of cards with random image/color
"""

import random
from enum import Enum, auto

N_ROWS = 4
N_COLS = 2


class Color(Enum):
    """Colors showed on cards"""

    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    ORANGE = (255, 128, 0)
    PURPLE = (255, 0, 255)
    CYAN = (0, 255, 255)


class Image(Enum):
    """Images showed on cards"""

    DONUT = auto()
    SQUARE = auto()
    DIAMOND = auto()
    LINES = auto()
    OVAL = auto()


# shapes - what the player sees
DONUT = "donut"
SQUARE = "square"
DIAMOND = "diamond"
LINES = "lines"
OVAL = "oval"
SHAPES = (DONUT, SQUARE, DIAMOND, LINES, OVAL)


def build_board():
    """A shuffled matrix that could contain any possible image in any possible color"""

    # shuffle all the image/color combinations
    items = [(image, color) for color in Color for image in Image]
    random.shuffle(items)

    # take just the required ones, make them double, and shuffle
    count = N_COLS * N_ROWS // 2
    items = items[:count] * 2
    random.shuffle(items)

    return [items[i : i + N_COLS] for i in range(0, len(items), N_COLS)]


if __name__ == "__main__":
    print(build_board())
