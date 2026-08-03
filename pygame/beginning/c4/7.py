"""
Setting pixels

From: Beginning Python Games Development with PyGame - https://link.springer.com/book/10.1007/978-1-4842-0970-7
My reviewed version: https://github.com/egalli64/pythonesque folder pygame/beginning
"""
import pygame
from random import randint, randrange

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    color = (randint(0, 255), randint(0, 255), randint(0, 255))
    for _ in range(100):
        pos = (randrange(0, SCREEN_WIDTH), randrange(0, SCREEN_HEIGHT))
        # that's a slow way to interact with the screen - use it only when strictly required
        screen.set_at(pos, color)
    pygame.display.flip()

pygame.quit()
