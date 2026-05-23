"""
Rectangles

From: Beginnning Python Games Development with PyGame - https://link.springer.com/book/10.1007/978-1-4842-0970-7
My reviewed version: https://github.com/egalli64/pythonesque/pygame/beginning
"""

import pygame
from random import randint, randrange

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

BACKGROUND_COLOR = (0, 0, 0)  # black

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)


def random_rect(pos):
    """Draw a random rectangle in the given position"""
    color = (randint(0, 255), randint(0, 255), randint(0, 255))
    width = SCREEN_WIDTH - randrange(pos[0], SCREEN_WIDTH)
    height = SCREEN_HEIGHT - randrange(pos[1], SCREEN_HEIGHT)
    pygame.draw.rect(screen, color, pygame.Rect(pos, (width, height)))


running = True
while running:
    event = pygame.event.wait(1000)
    screen.fill(BACKGROUND_COLOR)

    if event.type == pygame.QUIT:
        running = False
    elif event.type == pygame.NOEVENT:
        # in case of timeout on wait
        screen.lock()
        for _ in range(10):
            pos = (randrange(SCREEN_WIDTH), randrange(SCREEN_HEIGHT))
            random_rect(pos)
        screen.unlock()
        pygame.display.flip()
    elif event.type == pygame.MOUSEMOTION and event.rel != (0, 0):
        # in case of mouse motion (avoid no-motion, checking rel)
        random_rect(event.pos)
        pygame.display.flip()

print("Done.")
pygame.quit()
