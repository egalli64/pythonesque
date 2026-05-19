"""
Memory Puzzle - A simple memory matching game

From: Making Games with Python & Pygame by Al Sweigart - https://inventwithpython.com/pygame/
My reviewed version: https://github.com/egalli64/pythonesque/pygame/makinggames

Step 1d: draw the board
"""

from enum import Enum, auto
import pygame

FPS = 10

N_COLS = 2
N_ROWS = 2
BOX_SIZE = 40
GAP_SIZE = 10

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
SCREEN_TITLE = "Memory Game"

X_MARGIN = (SCREEN_WIDTH - (N_COLS * (BOX_SIZE + GAP_SIZE))) // 2
Y_MARGIN = (SCREEN_HEIGHT - (N_ROWS * (BOX_SIZE + GAP_SIZE))) // 2

NAVYBLUE = (60, 60, 100)
BACKGROUND_COLOR = NAVYBLUE


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


WHITE = (255, 255, 255)
BOX_COLOR = WHITE

# global pygame variables: frame clock and screen setup
# notice: encapsulation in a class would be a more robust option
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


def get_xy(i, j):
    """
    Convert position on board to pixel coordinates for the left-top corner

    For example: i = 0, j = 0 -> (270, 140); i = 0, j = 1 -> (320, 140)
    """
    return (j * (BOX_SIZE + GAP_SIZE) + X_MARGIN, i * (BOX_SIZE + GAP_SIZE) + Y_MARGIN)


def draw_card(_: Image, color: Color, x: int, y: int):
    """Draw the image/color card in position i, j - mock"""
    QUARTER = BOX_SIZE // 4
    HALF = BOX_SIZE // 2

    pygame.draw.ellipse(screen, color.value, (x, y + QUARTER, BOX_SIZE, HALF))


def draw_back_card(x, y):
    """Draw the card back in the given position"""
    pygame.draw.rect(screen, BOX_COLOR, (x, y, BOX_SIZE, BOX_SIZE))


def get_info(board, i, j):
    """Get image and color for the (i, j) card"""
    return board[i][j][0], board[i][j][1]


def draw_board(board, revealed):
    # Draws all of the boxes in their covered or revealed state.
    for i in range(N_ROWS):
        for j in range(N_COLS):
            x, y = get_xy(i, j)
            if not revealed[i][j]:
                draw_back_card(x, y)
            else:
                draw_card(*get_info(board, i, j), x, y)


def build_board():
    """A shuffled matrix that could contain any possible image in any possible color - mock"""

    return [
        [(None, Color.RED), (None, None)],
        [(None, None), (None, Color.BLUE)],
    ]


def main():
    """complete game setup and run the main game loop"""
    pygame.display.set_caption(SCREEN_TITLE)

    screen.fill(BACKGROUND_COLOR)

    draw_board(build_board(), [[True, False], [False, True]])

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()
        clock.tick(FPS)

    print("Done!")
    pygame.quit()


if __name__ == "__main__":
    main()
