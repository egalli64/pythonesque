"""
Using vectors for time-based movement

From: Beginnning Python Games Development with PyGame - https://link.springer.com/book/10.1007/978-1-4842-0970-7
My reviewed version: https://github.com/egalli64/pythonesque/pygame/beginning
"""

import pygame

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

BACKGROUND_IMG = "pygame/beginning/img/sushiplate.jpg"
SPRITE_IMG = "pygame/beginning/img/fugu.png"

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode(SCREEN_SIZE)
background = pygame.image.load(BACKGROUND_IMG).convert()
sprite = pygame.image.load(SPRITE_IMG).convert_alpha()

SPRITE_SPEED = 250
HALF_SPRITE = pygame.Vector2(sprite.get_size()) / 2
MIN_X = -HALF_SPRITE.x
MAX_X = SCREEN_WIDTH - HALF_SPRITE.x
MIN_Y = -HALF_SPRITE.y
MAX_Y = SCREEN_HEIGHT - HALF_SPRITE.y


def clamp(pos):
    """Ensure the sprite stays visible"""
    pos.x = max(min(pos.x, MAX_X), MIN_X)
    pos.y = max(min(pos.y, MAX_Y), MIN_Y)


pos = pygame.Vector2(100.0, 100.0)
heading = pygame.Vector2()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            heading = (pygame.Vector2(event.pos) - HALF_SPRITE - pos).normalize()

    if running:
        dt = clock.tick() / 1000

        pos += heading * dt * SPRITE_SPEED
        clamp(pos)

        screen.blit(background)
        screen.blit(sprite, pos)
        pygame.display.flip()

print("Done.")
pygame.quit()
