"""
Memory Puzzle - A simple memory matching game

From: Making Games with Python & Pygame by Al Sweigart - https://inventwithpython.com/pygame/
My reviewed version: https://github.com/egalli64/pythonesque/pygame/makinggames

Step 1c: draw a card
"""

from enum import Enum, auto
import pygame

FPS = 10

N_ROWS = 4
N_COLS = 2

BOX_SIZE = 40
GAP_SIZE = 10

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
SCREEN_TITLE = "Memory Game"

X_MARGIN = (SCREEN_WIDTH - (N_COLS * (BOX_SIZE + GAP_SIZE))) // 2
Y_MARGIN = (SCREEN_HEIGHT - (N_ROWS * (BOX_SIZE + GAP_SIZE))) // 2


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


NAVYBLUE = (60, 60, 100)
BACKGROUND_COLOR = NAVYBLUE


pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


def main():
    """complete game setup and run the main game loop"""
    pygame.display.set_caption(SCREEN_TITLE)

    screen.fill(BACKGROUND_COLOR)

    draw_card(Image.DONUT, Color.RED, *get_xy(0, 0))
    draw_card(Image.SQUARE, Color.BLUE, *get_xy(0, 1))
    draw_card(Image.DIAMOND, Color.GREEN, *get_xy(1, 0))
    draw_card(Image.LINES, Color.YELLOW, *get_xy(1, 1))
    draw_card(Image.OVAL, Color.ORANGE, *get_xy(2, 0))
    draw_card(Image.DONUT, Color.PURPLE, *get_xy(2, 1))
    draw_card(Image.SQUARE, Color.CYAN, *get_xy(3, 0))
    draw_card(Image.DIAMOND, Color.RED, *get_xy(3, 1))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()
        clock.tick(FPS)

    print("Done!")
    pygame.quit()


def get_xy(i, j):
    """
    Convert position on board to pixel coordinates for the left-top corner

    For example: i = 0, j = 0 -> (270, 140); i = 0, j = 1 -> (320, 140)
    """
    return (j * (BOX_SIZE + GAP_SIZE) + X_MARGIN, i * (BOX_SIZE + GAP_SIZE) + Y_MARGIN)


def draw_card(image: Image, color: Color, x: int, y: int):
    """Draw the image/color card from the top-left position x, y"""
    QUARTER = BOX_SIZE // 4
    HALF = BOX_SIZE // 2

    if image == Image.DONUT:
        pygame.draw.circle(screen, color.value, (x + HALF, y + HALF), HALF - 5)
        pygame.draw.circle(screen, BACKGROUND_COLOR, (x + HALF, y + HALF), QUARTER - 5)
    elif image == Image.SQUARE:
        area = (x + QUARTER, y + QUARTER, HALF, HALF)
        pygame.draw.rect(screen, color.value, area)
    elif image == Image.DIAMOND:
        area = (
            (x + HALF, y),
            (x + BOX_SIZE - 1, y + HALF),
            (x + HALF, y + BOX_SIZE - 1),
            (x, y + HALF),
        )
        pygame.draw.polygon(screen, color.value, area)
    elif image == Image.LINES:
        for i in range(0, BOX_SIZE, 4):
            pygame.draw.line(screen, color.value, (x, y + i), (x + i, y))
            start_end = (x + i, y + BOX_SIZE - 1), (x + BOX_SIZE - 1, y + i)
            pygame.draw.line(screen, color.value, *start_end)
    elif image == Image.OVAL:
        pygame.draw.ellipse(screen, color.value, (x, y + QUARTER, BOX_SIZE, HALF))


if __name__ == "__main__":
    main()
