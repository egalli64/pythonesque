"""
Memory Puzzle - A simple memory matching game

From: Making Games with Python & Pygame by Al Sweigart - https://inventwithpython.com/pygame/
My reviewed version: https://github.com/egalli64/pythonesque/pygame/makinggames

Step 3b: MOUSEBUTTONUP event - make the second card visible
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

X_MARGIN = (SCREEN_WIDTH - (N_COLS * BLOCK_SIZE)) // 2
Y_MARGIN = (SCREEN_HEIGHT - (N_ROWS * BLOCK_SIZE)) // 2


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
    """mock"""
    items = [(image, color) for color in Color for image in Image]
    count = N_COLS * N_ROWS // 2
    items = items[:count] * 2
    return [items[i : i + N_COLS] for i in range(0, len(items), N_COLS)]


pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
visibility = [[False] * N_COLS for _ in range(N_ROWS)]
board = build_board()
print(board)


class GameColor:
    """Colors in the game (not in the cards)"""

    CARD_BACK = (255, 255, 255)  # white
    BACKGROUND = (60, 60, 100)  # navy blue
    HIGHLIGHT = (173, 216, 230)  # light blue


def get_card_info(i: int, j: int):
    """Get image and color for the (i, j) card"""
    return board[i][j]


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
            pygame.display.flip()


def get_card_pos(xy):
    """mock"""
    if 195 < xy[0] < 235 and 240 < xy[1] < 270:
        return (195, 240), (1, 4)
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


def cover_cards(xy_cards):
    """mock"""
    for xy in xy_cards:
        print("Covering", xy)


def get_xy(i: int, j: int):
    return j * BLOCK_SIZE + X_MARGIN, i * BLOCK_SIZE + Y_MARGIN


def check_match(first, second):
    """Compare two cards, turn them back if they don't match"""
    card_1 = get_card_info(*first)
    card_2 = get_card_info(*second)
    if card_1 != card_2:
        cover_cards([get_xy(*first), get_xy(*second)])
        visibility[first[0]][first[1]] = False
        visibility[second[0]][second[1]] = False
    else:
        print(f"{first} matches {second}")


def main():
    # for mocking
    draw_back_card(195, 240)  # the target for the second card
    pygame.display.flip()
    # mocking a previous click on this card
    first_card = (0, 0)
    visibility[0][0] = True

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONUP:
                if ij := select_card(get_card_pos(event.pos)):
                    if first_card:
                        check_match(first_card, ij)
                    else:
                        first_card = ij
                print(f"Revealed card: {ij}, first_card: {first_card}")

    print("Done!")
    pygame.quit()


if __name__ == "__main__":
    main()
