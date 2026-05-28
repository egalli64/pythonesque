"""
Sprite Group

From: A Primer on Pygame Game Programming - https://realpython.com/pygame-a-primer/
My reviewed version: https://github.com/egalli64/pythonesque/pygame/primer
"""

from typing import override
import pygame
import random

FPS = 30

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_SIZE = pygame.Vector2(SCREEN_WIDTH, SCREEN_HEIGHT)
SCREEN_CENTER = SCREEN_SIZE / 2
SCREEN_RECT = (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)

BACKGROUND_COLOR = (0, 0, 0)  # black

PLAYER_COLOR = (255, 255, 255)  # white
PLAYER_SIZE = pygame.Vector2(75, 25)
PLAYER_SPEED = 200

ENEMY_COLOR = (255, 0, 0)  # red
ENEMY_SIZE = pygame.Vector2(20, 10)
ENEMY_MIN_SPEED = 100
ENEMY_MAX_SPEED = 200


class Player(pygame.sprite.Sprite):
    image: pygame.Surface
    rect: pygame.Rect

    @override
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface(PLAYER_SIZE)  # type: ignore
        self.image.fill(PLAYER_COLOR)
        self.rect = self.image.get_rect(center=SCREEN_CENTER)  # type: ignore

    @override
    def update(self, pressed_keys, dt):
        """
        Move in place the sprite based on the keys pressed

        Keep it inside the screen area
        """
        delta_pixel = PLAYER_SPEED * dt
        dpos = pygame.Vector2()

        if pressed_keys[pygame.K_RIGHT]:
            dpos.x += delta_pixel
        if pressed_keys[pygame.K_DOWN]:
            dpos.y += delta_pixel
        if pressed_keys[pygame.K_LEFT]:
            dpos.x -= delta_pixel
        if pressed_keys[pygame.K_UP]:
            dpos.y -= delta_pixel

        self.rect.move_ip(dpos)
        self.rect.clamp_ip(SCREEN_RECT)


class Enemy(pygame.sprite.Sprite):
    image: pygame.Surface
    rect: pygame.Rect

    @override
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface(ENEMY_SIZE)  # type: ignore
        self.image.fill(ENEMY_COLOR)

        # take off somewhere out of screen to the right
        x = random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100)
        y = random.randint(0, SCREEN_HEIGHT)
        self.rect = self.image.get_rect(center=(x, y))  # type: ignore
        self.speed = random.randint(ENEMY_MIN_SPEED, ENEMY_MAX_SPEED)

    # adding a method to the class
    @override
    def update(self, dt):
        """
        Move the sprite based on speed

        Remove the sprite from each group when it passes the left edge of the screen
        """
        dx = -self.speed * dt
        self.rect.move_ip(dx, 0)
        if self.rect.right < 0:
            self.kill()


pygame.init()

screen = pygame.display.set_mode(SCREEN_SIZE)
player = Player()
an_enemy = Enemy()  # temporary generate a single enemy
clock = pygame.time.Clock()

# more robust sprites management
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()

all_sprites.add(player)
all_sprites.add(an_enemy)
enemies.add(an_enemy)
# change ends here

running = True
while running:
    dt = clock.tick(30) / 1000

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        elif event.type == pygame.QUIT:
            running = False

    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys, dt)

    # update all enemies in one go
    enemies.update(dt)

    screen.fill(BACKGROUND_COLOR)

    # draw all sprites in one go
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
    # change ends here

    pygame.display.flip()

print("Done.")
pygame.quit()
