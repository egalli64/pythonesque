"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Collision between a sprite and a group of sprites
"""

from enum import Enum
from typing import override

import pygame

FPS = 30
TITLE = "Collision"
WIN_RECT = pygame.Rect(0, 0, 640, 480)
BACKGROUND_COLOR = (30, 30, 30)
TEXT_COLOR = (200, 200, 200)
TEXT_POS = (10, 10)
FONT_SIZE = 24


class Player(pygame.sprite.Sprite):
    START_POS = (320, 240)
    SIZE = (40, 40)
    COLOR = (50, 200, 50)
    SPEED = 100

    class Direction(Enum):
        STOP = pygame.Vector2(0, 0)
        RIGHT = pygame.Vector2(1, 0)
        LEFT = pygame.Vector2(-1, 0)
        UP = pygame.Vector2(0, -1)
        DOWN = pygame.Vector2(0, 1)

    def __init__(self):
        super().__init__()
        self.image = pygame.Surface(Player.SIZE)
        self.image.fill(Player.COLOR)
        self.rect: pygame.Rect = self.image.get_rect(center=Player.START_POS)
        self.direction = Player.Direction.STOP.value

    def set_direction(self, direction: Direction) -> None:
        self.direction = direction.value

    @override
    def update(self, dt) -> None:
        self.rect.move_ip(Player.SPEED * self.direction * dt)
        self.rect.clamp_ip(WIN_RECT)


class Block(pygame.sprite.Sprite):
    COLOR = (200, 50, 50)
    SIZE = (30, 30)

    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface(Block.SIZE)
        self.image.fill(Block.COLOR)
        self.rect = self.image.get_rect(center=pos)


def get_direction() -> Player.Direction:
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        return Player.Direction.LEFT
    elif keys[pygame.K_RIGHT]:
        return Player.Direction.RIGHT
    elif keys[pygame.K_UP]:
        return Player.Direction.UP
    elif keys[pygame.K_DOWN]:
        return Player.Direction.DOWN
    else:
        return Player.Direction.STOP


def handle_events() -> bool:
    """Run the event loops, return False in case of termination request"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False
    return True


def main():
    window = pygame.Window(TITLE, WIN_RECT.size)
    screen = window.get_surface()
    clock = pygame.time.Clock()

    player = Player()
    blocks = pygame.sprite.Group()
    for x in range(80, 600, 80):
        for y in range(120, 400, 80):
            blocks.add(Block((x, y)))

    all_sprites = pygame.sprite.Group(player, *blocks.sprites())

    font = pygame.font.SysFont(None, FONT_SIZE)

    while handle_events():
        dt = clock.tick(FPS) / 1000

        # update
        player.set_direction(get_direction())
        player.update(dt)

        # no callback passed to determine collision -> rects are used
        pygame.sprite.spritecollide(player, blocks, True)

        # rendering
        screen.fill(BACKGROUND_COLOR)
        all_sprites.draw(screen)
        text = font.render(f"Blocks remaining: {len(blocks)}", True, TEXT_COLOR)
        screen.blit(text, TEXT_POS)

        window.flip()


if __name__ == "__main__":
    pygame.init()

    try:
        main()
    finally:
        pygame.quit()
        print("Done.")
