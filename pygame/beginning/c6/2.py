"""
Arrow keys for movement

From: Beginnning Python Games Development with PyGame - https://link.springer.com/book/10.1007/978-1-4842-0970-7
My reviewed version: https://github.com/egalli64/pythonesque/pygame/beginning
"""

import pygame

SCREEN_SIZE = pygame.Vector2(640, 480)

BACKGROUND_IMG = "pygame/beginning/img/sushiplate.jpg"
SPRITE_IMG = "pygame/beginning/img/fugu.png"

pygame.init()

screen = pygame.display.set_mode(SCREEN_SIZE)
background = pygame.image.load(BACKGROUND_IMG).convert()
sprite = pygame.image.load(SPRITE_IMG).convert_alpha()
clock = pygame.time.Clock()

sprite_pos = pygame.Vector2(200, 150)
SPRITE_SPEED = 300

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if running:
        dt = clock.tick(30) / 1000

        keys = pygame.key.get_pressed()
        direction = pygame.Vector2()
        if keys[pygame.K_LEFT]:
            direction.x -= 1
        if keys[pygame.K_RIGHT]:
            direction.x += 1
        if keys[pygame.K_UP]:
            direction.y -= 1
        if keys[pygame.K_DOWN]:
            direction.y += 1

        if direction:
            direction.normalize_ip()
            sprite_pos += direction * SPRITE_SPEED * dt

        screen.blit(background)
        screen.blit(sprite, sprite_pos)
        pygame.display.flip()

print("Done.")
pygame.quit()
