"""
Ellipses

From: Beginnning Python Games Development with PyGame - https://link.springer.com/book/10.1007/978-1-4842-0970-7
My reviewed version: https://github.com/egalli64/pythonesque/pygame/beginning
"""

import pygame

SCREEN_SIZE = (640, 480)
BACKGROUND_COLOR = (255, 255, 255)  # white
ELLIPSE_COLOR = (0, 255, 0)  # green

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if running:
        screen.fill(BACKGROUND_COLOR)

        pygame.draw.ellipse(screen, ELLIPSE_COLOR, (0, 0, *pygame.mouse.get_pos()))
        pygame.display.flip()

print("Done.")
pygame.quit()
