"""
Time-Based Movement (better, but still no frame control)

From: Beginnning Python Games Development with PyGame - https://link.springer.com/book/10.1007/978-1-4842-0970-7
My reviewed version: https://github.com/egalli64/pythonesque/pygame/beginning
"""

import pygame

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

BACKGROUND_IMG = "pygame/beginning/img/sushiplate.jpg"
SPRITE_IMG = "pygame/beginning/img/fugu.png"
SPRITE_Y = 100
SPEED = 250  # pixel per sec.

pygame.init()

screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()

background = pygame.image.load(BACKGROUND_IMG).convert()
sprite = pygame.image.load(SPRITE_IMG).convert_alpha()

sprite_x = 0

running = True
while running:
    # keep the movement as indipendent as possible to the machine actually running the code
    dt = clock.tick() / 1000
    candidate_x = sprite_x + SPEED * dt
    sprite_x = candidate_x if candidate_x < SCREEN_WIDTH else 0

    screen.blit(background)
    screen.blit(sprite, (sprite_x, SPRITE_Y))
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

print("Done.")
pygame.quit()
