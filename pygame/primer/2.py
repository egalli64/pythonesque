"""
Game structure: initialize, setup the display, process events, quit

From: A Primer on Pygame Game Programming - https://realpython.com/pygame-a-primer/
My reviewed version: https://github.com/egalli64/pythonesque/pygame/primer
"""

# (a) Importing and Initializing Pygame
import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_SIZE = pygame.Vector2(SCREEN_WIDTH, SCREEN_HEIGHT)

pygame.init()

# (b) Setting Up the Display
screen = pygame.display.set_mode(SCREEN_SIZE)

# (c) Processing Events
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        elif event.type == pygame.QUIT:
            running = False


print("Done.")
pygame.quit()
