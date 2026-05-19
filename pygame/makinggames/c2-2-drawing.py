"""
Primitive Drawing Functions

From: Making Games with Python & Pygame by Al Sweigart - https://inventwithpython.com/pygame/
"""

import pygame
import sys

# main pygame screen constants
SCREEN_SIZE = (500, 400)
SCREEN_TITLE = "Drawing"

pygame.init()

# set up the window
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
pygame.display.set_caption(SCREEN_TITLE)

# set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# draw on the surface object
screen.fill(WHITE)

# a green polygon
POLY_POINTS = ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106))
pygame.draw.polygon(screen, GREEN, POLY_POINTS)

# three blue lines making a zed
pygame.draw.line(screen, BLUE, (60, 60), (120, 60), 4)
pygame.draw.line(screen, BLUE, (120, 60), (60, 120))
pygame.draw.line(screen, BLUE, (60, 120), (120, 120), 4)

# a blue circle
pygame.draw.circle(screen, BLUE, (300, 50), 20, 0)

# a red ellipse
pygame.draw.ellipse(screen, RED, (300, 250, 40, 80), 1)

# a red rectangle
pygame.draw.rect(screen, RED, (200, 150, 100, 50))

# five black points

# Using PixelArray makes sense performancewise, in case of many points
# pixObj = pygame.PixelArray(screen)
# pixObj[480][380] = BLACK
# ...
# del pixObj

# for few points use set_at() instead
for point in ((480, 380), (482, 382), (484, 384), (486, 386), (488, 388)):
    screen.set_at(point, BLACK)

# run the game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()
