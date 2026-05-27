"""
Sprite - a game entity

From: A Primer on Pygame Game Programming - https://realpython.com/pygame-a-primer/
My reviewed version: https://github.com/egalli64/pythonesque/pygame/primer
"""

import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_SIZE = pygame.Vector2(SCREEN_WIDTH, SCREEN_HEIGHT)
SCREEN_CENTER = SCREEN_SIZE / 2

BACKGROUND_COLOR = (0, 0, 0)  # black
PLAYER_COLOR = (255, 255, 255)  # white
PLAYER_SIZE = pygame.Vector2(75, 25)


class Player(pygame.sprite.Sprite):
    """
    Player is-a drawable Sprite

    So, a Surface and a Rect is provided
    """

    image: pygame.Surface
    rect: pygame.Rect

    def __init__(self):
        super().__init__()
        self.image = pygame.Surface(PLAYER_SIZE)  # type: ignore
        self.image.fill(PLAYER_COLOR)
        # let's pygame adjust the rect for us
        self.rect = self.image.get_rect(center=SCREEN_CENTER)  # type: ignore


pygame.init()

screen = pygame.display.set_mode(SCREEN_SIZE)
player = Player()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        elif event.type == pygame.QUIT:
            running = False

    screen.fill(BACKGROUND_COLOR)

    screen.blit(player.image, player.rect)
    pygame.display.flip()

print("Done.")
pygame.quit()
