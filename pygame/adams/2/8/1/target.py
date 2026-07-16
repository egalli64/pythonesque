"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Sprite collisions
"""
from enum import Enum, auto

import pygame


class Target(pygame.sprite.Sprite):
    class Kind(Enum):
        BRICK = auto()
        SHIP = auto()
        ALIEN = auto()

    FILENAMES = {
        Kind.BRICK: ("../../images/brick_1.png", "../../images/brick_2.png"),
        Kind.SHIP: ("../../images/ship_1.png", "../../images/ship_2.png"),
        Kind.ALIEN: ("../../images/alien_big_1.png", "../../images/alien_big_2.png"),
    }

    image: pygame.Surface
    rect: pygame.Rect

    @classmethod
    def load_resources(cls):
        cls._images = {}

        for kind, (normal, highlight) in cls.FILENAMES.items():
            cls._images[kind] = (
                pygame.image.load(normal).convert_alpha(),
                pygame.image.load(highlight).convert_alpha(),
            )

    def __init__(self, y_pos: int, kind: Kind) -> None:
        super().__init__()

        self.image = Target._images[kind][0]
        self.rect = self.image.get_rect()
        self.rect.centery = y_pos

        self.radius = min(self.rect.size) // 2  # see pygame.sprite.collide_circle()
        self.mask = pygame.mask.from_surface(self.image)  # see pygame.sprite.collide_mask()

        self.kind = kind

    def highlight(self, active: bool) -> None:
        self.image = Target._images[self.kind][active]
