"""
Arc

From: Beginnning Python Games Development with PyGame - https://link.springer.com/book/10.1007/978-1-4842-0970-7
My reviewed version: https://github.com/egalli64/pythonesque/pygame/beginning
"""

import pygame
import math

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

BACKGROUND_COLOR = (255, 255, 255)  # white
ARC_COLOR = (0, 0, 0)  # black
ARC_START_ANGLE = 0
ARC_AREA = (1, 1, SCREEN_WIDTH - 1, SCREEN_HEIGHT - 1)

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        else:
            x, _ = pygame.mouse.get_pos()
            # angle in radians
            stop_angle = (x / (SCREEN_WIDTH - 1)) * math.pi * 2
            screen.fill(BACKGROUND_COLOR)
            pygame.draw.arc(screen, ARC_COLOR, ARC_AREA, ARC_START_ANGLE, stop_angle)
            pygame.display.flip()

print("Done.")
pygame.quit()
