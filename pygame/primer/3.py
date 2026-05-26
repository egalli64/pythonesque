"""
Drawing on the screen

From: A Primer on Pygame Game Programming - https://realpython.com/pygame-a-primer/
My reviewed version: https://github.com/egalli64/pythonesque/pygame/primer
"""

import pygame

SCREEN_SIZE = pygame.Vector2(800, 600)
SCREEN_CENTER = SCREEN_SIZE / 2

# begin new stuff
BACKGROUND_COLOR = (255, 255, 255)  # white
SURF_COLOR = (0, 0, 0)  # black
SURF_SIZE = pygame.Vector2(50, 50)
SURF_POS = SCREEN_CENTER - SURF_SIZE / 2
# end new stuff

pygame.init()

screen = pygame.display.set_mode(SCREEN_SIZE)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        elif event.type == pygame.QUIT:
            running = False

    # begin new stuff
    screen.fill(BACKGROUND_COLOR)

    surf = pygame.Surface(SURF_SIZE)
    surf.fill(SURF_COLOR)

    screen.blit(surf, SURF_POS)
    pygame.display.flip()
    # end new stuff

print("Done.")
pygame.quit()
