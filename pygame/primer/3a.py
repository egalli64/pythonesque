"""
User input - move the player

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
    """
    Player is-a drawable Sprite

    So, a Surface and a Rect is provided
    """

    rect: pygame.Rect  # in here rect is always a Rect

    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface(SURF_SIZE)
        self.surf.fill(SURF_COLOR)
        self.rect = self.surf.get_rect()  # type: ignore - hide Pylance complaint

    # new method
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


pygame.init()

screen = pygame.display.set_mode(SCREEN_SIZE)
SCREEN_RECT = screen.get_rect()
player = Player()

running = True
while running:
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
    screen.blit(player.surf, player.rect)
    pygame.display.flip()

print("Done.")
pygame.quit()
