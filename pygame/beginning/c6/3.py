"""
Free Rotation Control

From: Beginnning Python Games Development with PyGame - https://link.springer.com/book/10.1007/978-1-4842-0970-7
My reviewed version: https://github.com/egalli64/pythonesque/pygame/beginning
"""

import pygame
import math

FPS = 30

SCREEN_SIZE = pygame.Vector2(640, 480)
BACKGROUND_IMG = "pygame/beginning/img/sushiplate.jpg"
SPRITE_IMG = "pygame/beginning/img/fugu.png"

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode(SCREEN_SIZE)
background = pygame.image.load(BACKGROUND_IMG).convert()
sprite = pygame.image.load(SPRITE_IMG).convert_alpha()

SPRITE_SPEED = 300
SPRITE_ROTATION_SPEED = 360  # degrees per second
sprite_pos = pygame.Vector2(200, 150)
sprite_angle = 0  # degrees

running = True
while running:
    td = clock.tick(FPS) / 1000

    screen.blit(background)

    pressed_keys = pygame.key.get_pressed()

    # adjust the sprite angle
    rotation = 0
    if pressed_keys[pygame.K_LEFT]:
        rotation = 1
    if pressed_keys[pygame.K_RIGHT]:
        rotation = -1

    sprite_angle += rotation * SPRITE_ROTATION_SPEED * td
    rotated_sprite = pygame.transform.rotate(sprite, sprite_angle)

    # adjust the sprite position
    direction = 0
    if pressed_keys[pygame.K_UP]:
        direction = 1
    if pressed_keys[pygame.K_DOWN]:
        direction = -1

    if direction:
        rad = math.radians(sprite_angle)
        # notice the minus in the y component!
        # heading = pygame.Vector2(math.cos(rad), -math.sin(rad))
        heading = pygame.Vector2(1, 0).rotate(-sprite_angle)

        sprite_pos += direction * heading * SPRITE_SPEED * td

    # visualize the moved sprite
    rotated_size = pygame.Vector2(rotated_sprite.get_size())
    sprite_draw_pos = sprite_pos - rotated_size / 2

    screen.blit(rotated_sprite, sprite_draw_pos)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

print("Done.")
pygame.quit()
