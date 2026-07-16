"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Sprite collisions
"""
from enum import Enum, auto
from typing import override

import pygame


class Kind(Enum):
    BRICK = auto()
    SHIP = auto()
    ALIEN = auto()


FILENAMES = {
    Kind.BRICK: ("../images/brick_1.png", "../images/brick_2.png"),
    Kind.SHIP: ("../images/ship_1.png", "../images/ship_2.png"),
    Kind.ALIEN: ("../images/alien_big_1.png", "../images/alien_big_2.png"),
}


class Target(pygame.sprite.Sprite):
    image: pygame.Surface
    rect: pygame.Rect

    @classmethod
    def load_resources(cls):
        cls._images = {}

        for kind in Kind:
            cls._images[kind] = (
                pygame.image.load(FILENAMES[kind][0]).convert_alpha(),
                pygame.image.load(FILENAMES[kind][1]).convert_alpha()
            )

    def __init__(self, y_pos: int, kind: Kind) -> None:
        super().__init__()

        self.image = Target._images[kind][0]
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.radius = self.rect.centerx
        self.rect.centery = y_pos
        self.kind = kind

    @override
    def update(self, hit: bool) -> None:
        self.image = Target._images[self.kind][hit]
