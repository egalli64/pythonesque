"""
Basic Pygame Program

From: A Primer on Pygame Game Programming - https://realpython.com/pygame-a-primer/
My reviewed version: https://github.com/egalli64/pythonesque/pygame/primer
"""

import pygame

SCREEN_SIZE = pygame.Vector2(500, 500)
SCREEN_CENTER = SCREEN_SIZE / 2
BACKGROUND_COLOR = (255, 255, 255)  # white
CIRCLE_COLOR = (0, 0, 255)  # blue
CRICLE_RADIUS = 75

pygame.init()

screen = pygame.display.set_mode(SCREEN_SIZE)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BACKGROUND_COLOR)

    pygame.draw.circle(screen, CIRCLE_COLOR, SCREEN_CENTER, CRICLE_RADIUS)
    pygame.display.flip()

print("Done.")
pygame.quit()
