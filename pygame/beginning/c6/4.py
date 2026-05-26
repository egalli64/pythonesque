"""
Rotational Mouse Movement

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
screen = pygame.display.set_mode((640, 480), 0, 32)

clock = pygame.time.Clock()
background = pygame.image.load(BACKGROUND_IMG).convert()
sprite = pygame.image.load(SPRITE_IMG).convert_alpha()

# hide the mouse and give full control to pygame
pygame.mouse.set_visible(False)
pygame.event.set_grab(True)

SPRITE_SPEED = 300
SPRITE_ROTATION_SPEED = 360  # degrees per second
sprite_pos = pygame.Vector2(200, 150)
sprite_angle = 0  # degrees

HALF_SPRITE = pygame.Vector2(sprite.get_size()) / 2
MAX_X = SCREEN_SIZE.x - HALF_SPRITE.x
MAX_Y = SCREEN_SIZE.y - HALF_SPRITE.y


def clamp(pos):
    """Ensure the sprite stays visible"""
    pos.x = max(min(pos.x, MAX_X), 0)
    pos.y = max(min(pos.y, MAX_Y), 0)


running = True
while running:
    td = clock.tick(FPS) / 1000

    screen.blit(background)

    pressed_keys = pygame.key.get_pressed()
    pressed_mouse = pygame.mouse.get_pressed()

    # move the mouse left/right or use the arrow keys to rotate the sprite
    rotation = pygame.mouse.get_rel()[0]
    if pressed_keys[pygame.K_LEFT]:
        rotation = 1
    if pressed_keys[pygame.K_RIGHT]:
        rotation = -1

    sprite_angle += rotation * SPRITE_ROTATION_SPEED * td
    rotated_sprite = pygame.transform.rotate(sprite, sprite_angle)

    # click the mouse or use the arrow keys for direction
    direction = 0
    if pressed_keys[pygame.K_UP] or pressed_mouse[0]:
        direction = 1
    if pressed_keys[pygame.K_DOWN] or pressed_mouse[2]:
        direction = -1

    if direction:
        rad = math.radians(sprite_angle)
        heading = pygame.Vector2(1, 0).rotate(-sprite_angle)

        sprite_pos += direction * heading * SPRITE_SPEED * td
        clamp(sprite_pos)

    # visualize the moved sprite
    rotated_size = pygame.Vector2(rotated_sprite.get_size())
    sprite_draw_pos = sprite_pos - rotated_size / 2
    screen.blit(rotated_sprite, sprite_draw_pos)
    pygame.display.flip()

    for event in pygame.event.get():
        if (
            event.type == pygame.QUIT
            or event.type == pygame.KEYDOWN
            and event.key == pygame.K_ESCAPE
        ):
            running = False

print("Done.")
pygame.quit()
