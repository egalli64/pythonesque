"""
Frame rate and speed comparison - a slower machine would cause an unpleasent movement

From: Beginnning Python Games Development with PyGame - https://link.springer.com/book/10.1007/978-1-4842-0970-7
My reviewed version: https://github.com/egalli64/pythonesque/pygame/beginning
"""

import pygame

FPS = 30  # frame rate

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

BACKGROUND_IMG = "pygame/beginning/img/sushiplate.jpg"
SPRITE_IMG = "pygame/beginning/img/fugu.png"
SPRITE_1_Y = 50
SPRITE_2_Y = 250

pygame.init()

screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()
background = pygame.image.load(BACKGROUND_IMG).convert()
sprite = pygame.image.load(SPRITE_IMG).convert_alpha()

x_1 = 0
x_2 = 0
speed = 250  # pixels per second
frame_count = 0

running = True
while running:
    dt = clock.tick(FPS) / 1000

    # faster machine
    candidate = x_1 + dt * speed
    x_1 = candidate if candidate < SCREEN_WIDTH else 0

    # mocking a slower machine
    if (frame_count % 5) == 0:
        candidate = x_2 + (dt * speed) * 5
        x_2 = candidate if candidate < SCREEN_WIDTH else 0

    screen.blit(background)
    screen.blit(sprite, (x_1, SPRITE_1_Y))
    screen.blit(sprite, (x_2, SPRITE_2_Y))
    pygame.display.flip()
    frame_count += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

print("Done.")
pygame.quit()
