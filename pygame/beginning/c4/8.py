"""
Setting pixels w/locking

From: Beginnning Python Games Development with PyGame - https://link.springer.com/book/10.1007/978-1-4842-0970-7
My reviewed version: https://github.com/egalli64/pythonesque/pygame/beginning
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

    if running:
        color = (randint(0, 255), randint(0, 255), randint(0, 255))

        # lock is expensive, explicit lock on a group of locking calls mitigate the problem
        screen.lock()
        for _ in range(100):
            pos = (randrange(0, SCREEN_WIDTH), randrange(0, SCREEN_HEIGHT))
            screen.set_at(pos, color)
        screen.unlock()

        pygame.display.flip()

for x in range(10):
    xy = x, x + 1
    # getting a pixel could be very slow
    print(xy, screen.get_at(xy))

print("Done.")
pygame.quit()
