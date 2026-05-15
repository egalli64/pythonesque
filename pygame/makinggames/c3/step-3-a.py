"""
Memory Puzzle - A simple memory matching game

From: Making Games with Python & Pygame by Al Sweigart - https://inventwithpython.com/pygame/
My reviewed version: https://github.com/egalli64/pythonesque/pygame/makinggames

Step 3a: MOUSEBUTTONUP event - make the clicked card visible
"""

import pygame
from enum import Enum, auto

FPS = 30

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

CARD_SIZE = 40
GAP_SIZE = 10
BLOCK_SIZE = CARD_SIZE + GAP_SIZE
REVEAL_STEP = CARD_SIZE // 5

N_ROWS = 3
N_COLS = 6

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
visibility = [[False] * N_COLS for _ in range(N_ROWS)]


class GameColor:
    """Colors in the game (not in the cards)"""

    CARD_BACK = (255, 255, 255)  # white
    BACKGROUND = (60, 60, 100)  # navy blue
    HIGHLIGHT = (173, 216, 230)  # light blue


class Color(Enum):
    """Colors on cards"""

    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    ORANGE = (255, 128, 0)
    PURPLE = (255, 0, 255)
    CYAN = (0, 255, 255)


class Image(Enum):
    """Images on cards"""

    DONUT = auto()
    SQUARE = auto()
    DIAMOND = auto()
    LINES = auto()
    OVAL = auto()


def get_card_info(i: int, j: int):
    """mock"""
    return Image.DONUT, Color.CYAN


def draw_card(_: Image, color: Color, x: int, y: int):
    """mock"""
    QUARTER = CARD_SIZE // 4
    HALF = CARD_SIZE // 2

    pygame.draw.ellipse(screen, color.value, (x, y + QUARTER, CARD_SIZE, HALF))


def reveal_card(pos):
    """gradually reveal a card"""
    if pos:
        for back in range(CARD_SIZE, -1, -REVEAL_STEP):
            clock.tick(FPS)
            area = (*pos[0], CARD_SIZE, CARD_SIZE)
            pygame.draw.rect(screen, GameColor.BACKGROUND, area)
            draw_card(*get_card_info(*pos[1]), *pos[0])
            pygame.draw.rect(screen, GameColor.CARD_BACK, (*pos[0], back, CARD_SIZE))
            pygame.display.update()


def get_card_pos(xy):
    """mock"""
    if 195 < xy[0] < 235 and 240 < xy[1] < 270:
        return (195, 240), (2, 0)
    return None


def draw_back_card(x, y):
    pygame.draw.rect(screen, GameColor.CARD_BACK, (x, y, CARD_SIZE, CARD_SIZE))


def select_card(pos):
    """Reveal the card in the passed position, when required"""
    if pos and not visibility[pos[1][0]][pos[1][1]]:
        print("Click on", pos)
        reveal_card(pos)
        visibility[pos[1][0]][pos[1][1]] = True
        print(visibility)
        return pos[1]
    else:
        print("Current position (mock):", pos)
        return None


def main():
    # for mocking
    draw_back_card(195, 240)
    pygame.display.update()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONUP:
                ij = select_card(get_card_pos(event.pos))
                print("Revealed card:", ij)

    print("Done!")
    pygame.quit()


if __name__ == "__main__":
    main()
