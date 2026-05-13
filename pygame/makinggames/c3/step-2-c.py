"""
Memory Puzzle - A simple memory matching game

From: Making Games with Python & Pygame by Al Sweigart - https://inventwithpython.com/pygame/
My reviewed version: https://github.com/egalli64/pythonesque/pygame/makinggames

Step 2c: reveal a card
"""

import pygame
from enum import Enum, auto

FPS = 30

CARD_SIZE = 40
REVEAL_STEP = CARD_SIZE // 5

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


def get_card_pos(xy):
    """mock, see step 2a"""
    if xy[0] == 400:
        return (395, 140), (0, 4)
    else:
        return (195, 240), (2, 0)


def draw_card(_: Image, color: Color, x: int, y: int):
    """Draw the image/color card in position i, j - mock"""
    QUARTER = CARD_SIZE // 4
    HALF = CARD_SIZE // 2

    pygame.draw.ellipse(screen, color.value, (x, y + QUARTER, CARD_SIZE, HALF))


def cover_cards(xy_cards):
    """gradually cover the cards"""
    for coverage in range(0, CARD_SIZE + 1, REVEAL_STEP):
        clock.tick(FPS)
        for xy in xy_cards:
            pygame.draw.rect(screen, GameColor.CARD_BACK, (*xy, coverage, CARD_SIZE))
        pygame.display.update()


def get_card_info(i: int, j: int):
    """Get image and color for the (i, j) card - mock"""
    return Image.OVAL, Color.YELLOW


def reveal_cards(pos_cards):
    """gradually reveal the cards"""

    pos = pos_cards[0]

    for back in range(CARD_SIZE, -1, -REVEAL_STEP):
        for pos in pos_cards:
            clock.tick(FPS)
            pygame.draw.rect(screen, GameColor.BACKGROUND, (*pos[0], CARD_SIZE, CARD_SIZE))
            draw_card(*get_card_info(*pos[1]), *pos[0])
            pygame.draw.rect(screen, GameColor.CARD_BACK, (*pos[0], back, CARD_SIZE))
            pygame.display.update()


def main():
    pygame.display.set_caption(SCREEN_TITLE)
    clock.tick(FPS)

    screen.fill(GameColor.BACKGROUND)

    pos_cards = (get_card_pos((400, 0)), get_card_pos((200, 0)))
    xy_cards = (pos_cards[0][0], pos_cards[1][0])
    for xy in xy_cards:
        draw_card(Image.OVAL, Color.YELLOW, *xy)
    pygame.display.update()

    cover_cards(xy_cards)
    reveal_cards(pos_cards)

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
