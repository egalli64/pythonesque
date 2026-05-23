"""
Lines

From: Beginnning Python Games Development with PyGame - https://link.springer.com/book/10.1007/978-1-4842-0970-7
My reviewed version: https://github.com/egalli64/pythonesque/pygame/beginning
"""

import pygame

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

BACKGROUND_COLOR = (255, 255, 255)  # white
LINE_COLOR = (0, 255, 0)  # green
LINE_WIDTH = 5
MAX_LINE_POINTS = 100

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)

points = []

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        else:
            if event.type == pygame.MOUSEMOTION:
                points.append(event.pos)
                if len(points) > MAX_LINE_POINTS:
                    del points[0]

            screen.fill(BACKGROUND_COLOR)

            if len(points) > 1:
                pygame.draw.lines(screen, LINE_COLOR, False, points, LINE_WIDTH)

            pygame.display.flip()

pygame.quit()
