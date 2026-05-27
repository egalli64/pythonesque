"""
Sprites

From: A Primer on Pygame Game Programming - https://realpython.com/pygame-a-primer/
My reviewed version: https://github.com/egalli64/pythonesque/pygame/primer
"""

import pygame

SCREEN_SIZE = pygame.Vector2(800, 600)
SCREEN_CENTER = SCREEN_SIZE / 2

BACKGROUND_COLOR = (0, 0, 0)  # black
SURF_COLOR = (255, 255, 255)  # white
SURF_SIZE = pygame.Vector2(75, 25)
SURF_POS = SCREEN_CENTER - SURF_SIZE / 2


class Player(pygame.sprite.Sprite):
    """Player is-a Sprite"""

    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface(SURF_SIZE)
        self.surf.fill(SURF_COLOR)
        self.rect = self.surf.get_rect()


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

    screen.blit(player.surf, SCREEN_CENTER)
    pygame.display.flip()

print("Done.")
pygame.quit()
