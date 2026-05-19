"""
Memory Puzzle - A simple memory matching game

From: Making Games with Python & Pygame by Al Sweigart - https://inventwithpython.com/pygame/
My reviewed version: https://github.com/egalli64/pythonesque/pygame/makinggames

Step 3c: board reset when winning
"""

import pygame
from enum import Enum, auto

FPS = 30
CHEAT_TIME = 2000

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

N_ROWS = 3
N_COLS = 6

CARD_SIZE = 40
GAP_SIZE = 10
BLOCK_SIZE = CARD_SIZE + GAP_SIZE
REVEAL_STEP = CARD_SIZE // 5

X_MARGIN = (SCREEN_WIDTH - (N_COLS * BLOCK_SIZE)) // 2
Y_MARGIN = (SCREEN_HEIGHT - (N_ROWS * BLOCK_SIZE)) // 2


class GameColor:
    CARD_BACK = (255, 255, 255)  # white
    BACKGROUND = (60, 60, 100)  # navy blue
    HIGHLIGHT = (173, 216, 230)  # light blue
    ALT_BACKGROUND = (180, 120, 60)  # amber-orange


class Color(Enum):
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    ORANGE = (255, 128, 0)
    PURPLE = (255, 0, 255)
    CYAN = (0, 255, 255)


class Image(Enum):
    DONUT = auto()
    SQUARE = auto()
    DIAMOND = auto()
    LINES = auto()
    OVAL = auto()


def build_board():
    """Mock"""
    items = [(image, color) for color in Color for image in Image]
    count = N_COLS * N_ROWS // 2
    items = items[:count] * 2

    return [items[i : i + N_COLS] for i in range(0, len(items), N_COLS)]


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
visibility = [[False] * N_COLS for _ in range(N_ROWS)]
board = build_board()


def build_cards_visibility(x: bool):
    return [[x] * N_COLS for _ in range(N_ROWS)]


visibility = build_cards_visibility(False)


def flash_win():
    print("You have won!")
    c1 = GameColor.BACKGROUND
    c2 = GameColor.ALT_BACKGROUND

    for _ in range(10):
        c1, c2 = c2, c1
        screen.fill(c1)
        draw_board()
        pygame.display.flip()
        pygame.time.wait(300)


def winner():
    global visibility, board

    flash_win()
    visibility = build_cards_visibility(False)

    # board reset
    board = build_board()
    draw_board()
    pygame.display.flip()


def mock_game():
    for _ in range(2):
        for i in range(N_ROWS):
            for j in range(N_COLS):
                visibility[i][j] = True
            print(visibility)
            if all(all(row) for row in visibility):
                winner()


def draw_card(image: Image, color: Color, x: int, y: int):
    """mock"""
    QUARTER = CARD_SIZE // 4
    HALF = CARD_SIZE // 2

    center = (x + HALF, y + HALF)
    pygame.draw.circle(screen, color.value, center, HALF - 5)
    pygame.draw.circle(screen, GameColor.BACKGROUND, center, QUARTER - 5)


def draw_back_card(x, y):
    pygame.draw.rect(screen, GameColor.CARD_BACK, (x, y, CARD_SIZE, CARD_SIZE))


def get_xy(i: int, j: int):
    return j * BLOCK_SIZE + X_MARGIN, i * BLOCK_SIZE + Y_MARGIN


def draw_board():
    """mock"""
    for i in range(N_ROWS):
        for j in range(N_COLS):
            x, y = get_xy(i, j)
            if visibility[i][j]:
                draw_card(*board[i][j], x, y)
            else:
                draw_back_card(x, y)


def flash_cards():
    """mock"""
    draw_board()
    pygame.display.flip()


def main():
    flash_cards()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONUP:
                mock_game()

    print("Done!")
    pygame.quit()


if __name__ == "__main__":
    main()
