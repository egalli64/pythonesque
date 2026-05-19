"""
Memory Puzzle - A simple memory matching game

From: Making Games with Python & Pygame by Al Sweigart - https://inventwithpython.com/pygame/
My reviewed version: https://github.com/egalli64/pythonesque/pygame/makinggames

Step 2b: highlight a card, given its position
"""

import pygame

FPS = 1

CARD_SIZE = 40

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
SCREEN_TITLE = "Memory Game"


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
    elif xy[0] == 200:
        return (195, 240), (2, 0)
    else:
        return None


def highlight_card(pos, on=True):
    """Place a border around the card with the given position, or do nothing"""
    if pos:
        color = GameColor.HIGHLIGHT if on else GameColor.BACKGROUND
        area = (pos[0][0] - 5, pos[0][1] - 5, CARD_SIZE + 10, CARD_SIZE + 10)
        pygame.draw.rect(screen, color, area, 4)


def main():
    pygame.display.set_caption(SCREEN_TITLE)

    screen.fill(GameColor.BACKGROUND)

    highlight_card(get_card_pos((400, 0)))
    highlight_card(get_card_pos((200, 0)))
    highlight_card(get_card_pos((100, 0)))

    pygame.display.flip()

    running = True
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            highlight_card(get_card_pos((400, 0)), False)
            highlight_card(get_card_pos((200, 0)), False)
            highlight_card(get_card_pos((100, 0)), False)
            pygame.display.flip()

    print("Done!")
    pygame.quit()


if __name__ == "__main__":
    main()
