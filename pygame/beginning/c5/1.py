"""
Simple movement (too simple, no control on speed)

From: Beginning Python Games Development with PyGame - https://link.springer.com/book/10.1007/978-1-4842-0970-7
My reviewed version: https://github.com/egalli64/pythonesque folder pygame/beginning
"""
import pygame

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

BACKGROUND_IMG = "../img/sushiplate.jpg"
SPRITE_IMG = "../img/fugu.png"
SPRITE_Y = 100

pygame.init()

screen = pygame.display.set_mode(SCREEN_SIZE)

background = pygame.image.load(BACKGROUND_IMG).convert()
sprite = pygame.image.load(SPRITE_IMG).convert_alpha()

sprite_x = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # If the image goes off to the right then place it back to the left
    sprite_x = sprite_x + 1 if sprite_x < SCREEN_WIDTH else 0

    screen.blit(background)
    screen.blit(sprite, (sprite_x, SPRITE_Y))
    pygame.display.flip()

pygame.quit()
