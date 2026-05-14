"""
Memory Puzzle - A simple memory matching game

From: Making Games with Python & Pygame by Al Sweigart - https://inventwithpython.com/pygame/
My reviewed version: https://github.com/egalli64/pythonesque/pygame/makinggames

Step 2d: improved card flashing
"""

import pygame
from enum import Enum, auto

FPS = 30
CHEAT_TIME = 2000

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
SCREEN_TITLE = "Memory Game"

N_ROWS = 3
N_COLS = 6

CARD_SIZE = 40
REVEAL_STEP = CARD_SIZE // 5

CARD_SIZE = 40
GAP_SIZE = 10
BLOCK_SIZE = CARD_SIZE + GAP_SIZE

X_MARGIN = (SCREEN_WIDTH - (N_COLS * BLOCK_SIZE)) // 2
Y_MARGIN = (SCREEN_HEIGHT - (N_ROWS * BLOCK_SIZE)) // 2

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
SCREEN_TITLE = "Memory Game"


class Image(Enum):
    DONUT = auto()
    SQUARE = auto()
    DIAMOND = auto()
    LINES = auto()
    OVAL = auto()


class Color(Enum):
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    ORANGE = (255, 128, 0)
    PURPLE = (255, 0, 255)
    CYAN = (0, 255, 255)


class GameColor:
    CARD_BACK = (255, 255, 255)  # white
    BACKGROUND = (60, 60, 100)  # navy blue
    HIGHLIGHT = (173, 216, 230)  # light blue


pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


def get_card_info(i: int, j: int):
    """mock"""
    return Image.DONUT, Color.CYAN


def get_xy(i: int, j: int):
    return j * BLOCK_SIZE + X_MARGIN, i * BLOCK_SIZE + Y_MARGIN


def draw_card(_: Image, color: Color, x: int, y: int):
    """mock"""
    QUARTER = CARD_SIZE // 4
    HALF = CARD_SIZE // 2

    pygame.draw.ellipse(screen, color.value, (x, y + QUARTER, CARD_SIZE, HALF))


def draw_board(_):
    """mock"""
    for i in range(N_ROWS):
        for j in range(N_COLS):
            x, y = get_xy(i, j)
            draw_card(*get_card_info(i, j), x, y)


def cover_cards(xy_cards):
    """see step 2-c"""
    for coverage in range(0, CARD_SIZE + 1, REVEAL_STEP):
        clock.tick(FPS)
        for xy in xy_cards:
            pygame.draw.rect(screen, GameColor.CARD_BACK, (*xy, coverage, CARD_SIZE))
        pygame.display.update()


def flash_cards():
    """Show all the cards for a couple of seconds"""
    clock.tick(FPS)
    screen.fill(GameColor.BACKGROUND)

    draw_board(True)

    pygame.display.update()
    pygame.time.wait(CHEAT_TIME)

    for i in range(N_ROWS):
        card_group = []
        for j in range(N_COLS):
            card_group.append(get_xy(i, j))
        cover_cards(card_group)


def main():
    pygame.display.set_caption(SCREEN_TITLE)
    clock.tick(FPS)

    screen.fill(GameColor.BACKGROUND)

    flash_cards()

    running = True
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    print("Done!")
    pygame.quit()


if __name__ == "__main__":
    main()
