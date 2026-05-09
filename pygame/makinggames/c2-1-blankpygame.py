"""
Hello pygame

From: Making Games with Python & Pygame by Al Sweigart
Source: https://github.com/asweigart/making-games-with-python-and-pygame/blob/master/blankpygame/blankpygame.py
"""

import pygame
import sys

# main pygame screen constants
SCREEN_SIZE = (400, 300)
SCREEN_TITLE = "Hello World!"

# first of all, initialize pygame
pygame.init()

# create the main surface to work with
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption(SCREEN_TITLE)

# main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # terminate pygame
            pygame.quit()
            # terminate the python script
            sys.exit()
    # finalize the current frame, publishing (when required) the buffered changes
    pygame.display.update()
