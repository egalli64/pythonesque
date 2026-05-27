"""
Enemy - another Sprite

From: A Primer on Pygame Game Programming - https://realpython.com/pygame-a-primer/
My reviewed version: https://github.com/egalli64/pythonesque/pygame/primer
"""

import pygame
import random  # enemies behave in a random way

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_SIZE = pygame.Vector2(SCREEN_WIDTH, SCREEN_HEIGHT)
SCREEN_CENTER = SCREEN_SIZE / 2

BACKGROUND_COLOR = (0, 0, 0)  # black
SURF_COLOR = (255, 255, 255)  # white
SURF_SIZE = pygame.Vector2(75, 25)
SURF_POS = SCREEN_CENTER - SURF_SIZE / 2
ENEMY_COLOR = (255, 0, 0)  # red
ENEMY_SIZE = pygame.Vector2(20, 10)
ENEMY_MIN_SPEED = 5
ENEMY_MAX_SPEED = 20


class Player(pygame.sprite.Sprite):
    """
    Player is-a drawable Sprite

    So, a Surface and a Rect is provided
    """

    rect: pygame.Rect

    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface(SURF_SIZE)
        self.surf.fill(SURF_COLOR)
        self.rect = self.surf.get_rect()  # type: ignore

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


# new class
class Enemy(pygame.sprite.Sprite):
    """Enemy is-a drawable Sprite"""

    rect: pygame.Rect

    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.Surface(ENEMY_SIZE)
        self.surf.fill(ENEMY_COLOR)
        self.rect = self.surf.get_rect(  # type: ignore
            center=(
                # temporary place the enemy somewhere in the central screen area
                random.randint(SCREEN_WIDTH // 2 + 20, SCREEN_WIDTH // 2 + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )

        self.speed = random.randint(ENEMY_MIN_SPEED, ENEMY_MAX_SPEED)
        print(self.rect, self.speed)


pygame.init()

screen = pygame.display.set_mode(SCREEN_SIZE)
SCREEN_RECT = screen.get_rect()
player = Player()
an_enemy = Enemy()  # temporary generate a single enemy

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

    # temporary place an enemy on screen
    print(an_enemy.surf, an_enemy.rect)
    screen.blit(an_enemy.surf, an_enemy.rect)

    screen.blit(player.surf, player.rect)
    pygame.display.flip()

print("Done.")
pygame.quit()
