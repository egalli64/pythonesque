"""
Circle

From: Beginnning Python Games Development with PyGame - https://link.springer.com/book/10.1007/978-1-4842-0970-7
My reviewed version: https://github.com/egalli64/pythonesque/pygame/beginning
"""

import pygame
from random import randint, randrange

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
MIN_CIRCLE_RADIUS = 5
MAX_CIRCLE_RADIUS = 200

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)

for _ in range(25):
    color = (randint(0, 255), randint(0, 255), randint(0, 255))
    pos = (randrange(SCREEN_WIDTH), randrange(SCREEN_HEIGHT))
    radius = randint(MIN_CIRCLE_RADIUS, MAX_CIRCLE_RADIUS)
    pygame.draw.circle(screen, color, pos, radius)
    # alternative version: no fill, specified thickness
    # pygame.draw.circle(screen, color, pos, radius, 5)
    pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

print("Done.")
pygame.quit()
