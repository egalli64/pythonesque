"""
User input - move the player

From: A Primer on Pygame Game Programming - https://realpython.com/pygame-a-primer/
My reviewed version: https://github.com/egalli64/pythonesque/pygame/primer
"""

from typing import override
import pygame

FPS = 30  # frame per seconds

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_SIZE = pygame.Vector2(SCREEN_WIDTH, SCREEN_HEIGHT)
SCREEN_CENTER = SCREEN_SIZE / 2
SCREEN_RECT = (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)  # for player clamping

BACKGROUND_COLOR = (0, 0, 0)  # black
PLAYER_COLOR = (255, 255, 255)  # white
PLAYER_SIZE = pygame.Vector2(75, 25)
PLAYER_MOVE = 5  # pixel units


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
        self.rect = self.image.get_rect(center=SCREEN_CENTER)  # type: ignore

    # new method
    @override
    def update(self, pressed_keys):
        """
        Move in place the sprite based on the keys pressed

        Keep it inside the screen area
        """
        dpos = pygame.Vector2()

        if pressed_keys[pygame.K_RIGHT]:
            dpos.x += PLAYER_MOVE
        if pressed_keys[pygame.K_DOWN]:
            dpos.y += PLAYER_MOVE
        if pressed_keys[pygame.K_LEFT]:
            dpos.x -= PLAYER_MOVE
        if pressed_keys[pygame.K_UP]:
            dpos.y -= PLAYER_MOVE

        self.rect.move_ip(dpos)
        self.rect.clamp_ip(SCREEN_RECT)


pygame.init()

screen = pygame.display.set_mode(SCREEN_SIZE)
player = Player()
clock = pygame.time.Clock()  # manage the game frame rate

running = True
while running:
    clock.tick(30)  # give a human tempo to the game

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        elif event.type == pygame.QUIT:
            running = False

    # begin new stuff
    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)
    # end new stuff

    screen.fill(BACKGROUND_COLOR)

    # player position now is dynamic
    screen.blit(player.image, player.rect)
    pygame.display.flip()

print("Done.")
pygame.quit()
