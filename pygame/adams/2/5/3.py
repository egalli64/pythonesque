"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Sprite Group
"""

from enum import Enum, auto
import pygame

FPS = 30

TITLE = "Sprite"
WIN_RECT = pygame.Rect(0, 0, 600, 100)
WIN_POS = (10, 50)
BACKGROUND_COLOR = "white"


class Defender(pygame.sprite.Sprite):
    IMAGE = "../images/defender.png"
    SIZE = (30, 30)
    DEFAULT_SPEED = 150  # pixel/second
    BOTTOM_GAP = 5

    rect: pygame.FRect
    image: pygame.Surface

    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.image.load(Defender.IMAGE).convert_alpha()
        self.image = pygame.transform.scale(self.image, Defender.SIZE)  # type: ignore
        self.rect = pygame.FRect(self.image.get_rect())  # type: ignore
        self.rect.centerx = WIN_RECT.centerx
        self.rect.bottom = WIN_RECT.bottom - Defender.BOTTOM_GAP
        self.speed = 300

    def update(self, dt) -> None:
        self.rect.move_ip(self.speed * dt, 0)

    def change_direction(self) -> None:
        self.speed *= -1


class Border(pygame.sprite.Sprite):
    class Position(Enum):
        LEFT = auto()
        RIGHT = auto()

    IMAGE = "../images/brick.png"
    SIZE = (35, WIN_RECT.height)

    rect: pygame.Rect
    image: pygame.Surface

    def __init__(self, position: Position) -> None:
        super().__init__()
        self.image = pygame.image.load(Border.IMAGE).convert_alpha()
        self.image = pygame.transform.scale(self.image, Border.SIZE)  # type: ignore
        self.rect = self.image.get_rect()  # type: ignore
        if position == Border.Position.RIGHT:
            self.rect.right = WIN_RECT.right


def main():
    pygame.init()

    window = pygame.Window(TITLE, WIN_RECT.size, WIN_POS)
    screen = window.get_surface()
    clock = pygame.time.Clock()

    defender = pygame.sprite.GroupSingle(Defender())
    borders = pygame.sprite.Group()
    borders.add(Border(Border.Position.LEFT))
    borders.add(Border(Border.Position.RIGHT))

    running = True
    while running:
        dt = clock.tick(FPS) / 1000

        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update

        if pygame.sprite.spritecollide(defender.sprite, borders, False):  # type: ignore
            defender.sprite.change_direction()  # type: ignore
        defender.update(dt)

        # Draw
        screen.fill(BACKGROUND_COLOR)
        defender.draw(screen)  # the group knows how to draw its sprites
        borders.draw(screen)

        window.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
