"""
Memory Puzzle - A simple memory matching game

From: Making Games with Python & Pygame by Al Sweigart - https://inventwithpython.com/pygame/
My reviewed version: https://github.com/egalli64/pythonesque/pygame/makinggames

Step 2e: use mouse position to highlight the current card
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


def get_xy(i, j):
    """From step 1d"""
    return j * BLOCK_SIZE + X_MARGIN, i * BLOCK_SIZE + Y_MARGIN


def get_card_pos(xy):
    """From step 2a"""
    for i in range(N_ROWS):
        for j in range(N_COLS):
            top_left = get_xy(i, j)
            rect = pygame.Rect(*top_left, CARD_SIZE, CARD_SIZE)
            if rect.collidepoint(xy[0], xy[1]):
                return top_left, (i, j)
    return None


def highlight_card(pos, on=True):
    """From step 2b"""
    if pos:
        color = GameColor.HIGHLIGHT if on else GameColor.BACKGROUND
        area = (pos[0][0] - 5, pos[0][1] - 5, CARD_SIZE + 10, CARD_SIZE + 10)
        pygame.draw.rect(screen, color, area, 4)


def set_highlight(current):
    """Set the card in the mouse position to highlighted"""
    candidate = get_card_pos(pygame.mouse.get_pos())

    if candidate != current:
        clock.tick(FPS)

        highlight_card(current, False)
        highlight_card(candidate)
        pygame.display.update()

        return candidate
    else:
        return current


def main():
    pygame.display.set_caption(SCREEN_TITLE)
    clock.tick(FPS)
    screen.fill(GameColor.BACKGROUND)
    pygame.display.update()

    running = True
    current_card = None

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE
            ):
                running = False
            elif event.type == pygame.MOUSEMOTION:
                current_card = set_highlight(current_card)

    print("Done!")
    pygame.quit()


if __name__ == "__main__":
    main()
