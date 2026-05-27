"""
Sprite Group

From: A Primer on Pygame Game Programming - https://realpython.com/pygame-a-primer/
My reviewed version: https://github.com/egalli64/pythonesque/pygame/primer
"""

from typing import override

import pygame
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_SIZE = pygame.Vector2(SCREEN_WIDTH, SCREEN_HEIGHT)
SCREEN_CENTER = SCREEN_SIZE / 2

BACKGROUND_COLOR = (0, 0, 0)  # black
PLAYER_COLOR = (255, 255, 255)  # white
PLAYER_SIZE = pygame.Vector2(75, 25)
PLAYER_COLOR_POS = SCREEN_CENTER - PLAYER_SIZE / 2
ENEMY_COLOR = (255, 0, 0)  # red
ENEMY_SIZE = pygame.Vector2(20, 10)
ENEMY_MIN_SPEED = 5
ENEMY_MAX_SPEED = 20


class Player(pygame.sprite.Sprite):
    """
    Player is-a drawable Sprite

    So, a Surface and a Rect is provided
    """

    image: pygame.Surface
    rect: pygame.Rect

    @override
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface(PLAYER_SIZE)  # type: ignore
        self.image.fill(PLAYER_COLOR)
        self.rect = self.image.get_rect()  # type: ignore

    @override
    def update(self, pressed_keys):
        """
        Move in place the sprite based on the keys pressed

        Keep it inside the screen area
        """
        if pressed_keys[pygame.K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[pygame.K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[pygame.K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[pygame.K_RIGHT]:
            self.rect.move_ip(5, 0)

        self.rect.clamp_ip(SCREEN_RECT)


class Enemy(pygame.sprite.Sprite):
    """Enemy is-a drawable Sprite"""

    image: pygame.Surface
    rect: pygame.Rect

    @override
    def __init__(self):
        super(Enemy, self).__init__()
        self.image = pygame.Surface(ENEMY_SIZE)  # type: ignore
        self.image.fill(ENEMY_COLOR)
        self.rect = self.image.get_rect(  # type: ignore
            center=(
                # temporary place the enemy somewhere in the central screen area
                random.randint(SCREEN_WIDTH // 2 + 20, SCREEN_WIDTH // 2 + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )

        self.speed = random.randint(ENEMY_MIN_SPEED, ENEMY_MAX_SPEED)

    # adding a method to the class
    @override
    def update(self):
        """
        Move the sprite based on speed

        Remove the sprite from each group when it passes the left edge of the screen
        """
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()


pygame.init()

screen = pygame.display.set_mode(SCREEN_SIZE)
SCREEN_RECT = screen.get_rect()
player = Player()
an_enemy = Enemy()  # temporary generate a single enemy

# more robust sprites management
all_sprites = pygame.sprite.Group()

all_sprites.add(an_enemy)  # temporary manage a single enemy
all_sprites.add(player)
# change ends here

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        elif event.type == pygame.QUIT:
            running = False

    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)

    screen.fill(BACKGROUND_COLOR)

    # draw all sprites in one go
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
    # change ends here

    pygame.display.flip()

print("Done.")
pygame.quit()
