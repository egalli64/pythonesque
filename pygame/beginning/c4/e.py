"""
Line

From: Beginnning Python Games Development with PyGame - https://link.springer.com/book/10.1007/978-1-4842-0970-7
My reviewed version: https://github.com/egalli64/pythonesque/pygame/beginning
"""

import pygame

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

BACKGROUND_COLOR = (255, 255, 255)  # white
LINE_COLOR = (0, 0, 0)  # black

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        else:
            screen.fill(BACKGROUND_COLOR)

            pos = pygame.mouse.get_pos()

            for x in range(0, SCREEN_WIDTH, 40):
                pygame.draw.line(screen, LINE_COLOR, (x, 0), pos)
                pygame.draw.line(screen, LINE_COLOR, (x, SCREEN_HEIGHT), pos)

            for y in range(0, SCREEN_HEIGHT, 40):
                pygame.draw.line(screen, LINE_COLOR, (0, y), pos)
                pygame.draw.line(screen, LINE_COLOR, (SCREEN_WIDTH, y), pos)

            pygame.display.flip()

print("Done.")
pygame.quit()
