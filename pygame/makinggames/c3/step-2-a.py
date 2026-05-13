"""
Memory Puzzle - A simple memory matching game

From: Making Games with Python & Pygame by Al Sweigart - https://inventwithpython.com/pygame/
My reviewed version: https://github.com/egalli64/pythonesque/pygame/makinggames

Step 2a: find the coordinates for card colliding with the current mouse position
"""

import pygame

N_ROWS = 4
N_COLS = 5

CARD_SIZE = 40
GAP_SIZE = 10
BLOCK_SIZE = CARD_SIZE + GAP_SIZE


SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
SCREEN_TITLE = "Memory Game"

X_MARGIN = (SCREEN_WIDTH - (N_COLS * BLOCK_SIZE)) // 2
Y_MARGIN = (SCREEN_HEIGHT - (N_ROWS * BLOCK_SIZE)) // 2


def get_xy(i, j):
    """From step 1d"""
    return j * BLOCK_SIZE + X_MARGIN, i * BLOCK_SIZE + Y_MARGIN


def get_card_pos(xy):
    """Get the card xy (top-left) and ij coordinates, if we are in its rectangle"""
    for i in range(N_ROWS):
        for j in range(N_COLS):
            top_left = get_xy(i, j)
            rect = pygame.Rect(*top_left, CARD_SIZE, CARD_SIZE)
            if rect.collidepoint(xy[0], xy[1]):
                return top_left, (i, j)
    return None


if __name__ == "__main__":
    print(get_card_pos((400, 150)))
    print(get_card_pos((200, 245)))
    print(get_card_pos((500, 200)))
