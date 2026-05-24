"""
Simple Diagonal Movement

From: Beginnning Python Games Development with PyGame - https://link.springer.com/book/10.1007/978-1-4842-0970-7
My reviewed version: https://github.com/egalli64/pythonesque/pygame/beginning
"""

import pygame

BACKGROUND_IMG = "pygame/beginning/img/sushiplate.jpg"
SPRITE_IMG = "pygame/beginning/img/fugu.png"

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

FPS = 30

pygame.init()

screen = pygame.display.set_mode(SCREEN_SIZE)
background = pygame.image.load(BACKGROUND_IMG).convert()
sprite = pygame.image.load(SPRITE_IMG).convert_alpha()
clock = pygame.time.Clock()

MAX_X = SCREEN_WIDTH - sprite.get_width()
MAX_Y = SCREEN_HEIGHT - sprite.get_height()

x, y = 100, 100
speed_x, speed_y = 133, 170

running = True
while running:
    dt = clock.tick(FPS) / 1000

    # move the sprite with the current speed, or bounce
    x += speed_x * dt
    if x < 0 or x > MAX_X:
        speed_x *= -1
        x = 0 if x < 0 else MAX_X

    y += speed_y * dt
    if y < 0 or y > MAX_Y:
        speed_y *= -1
        y = 0 if y < 0 else MAX_Y

    screen.blit(background)
    screen.blit(sprite, (x, y))
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


print("Done.")
pygame.quit()
