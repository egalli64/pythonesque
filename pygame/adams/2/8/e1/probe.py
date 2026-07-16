"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Sprite collisions
"""
from enum import Enum
from typing import override

import pygame

INITIAL_CENTER = (10, 10)

class Direction(Enum):
    STOP = pygame.Vector2(0, 0)
    RIGHT = pygame.Vector2(1, 0)
    LEFT = pygame.Vector2(-1, 0)
    UP = pygame.Vector2(0, -1)
    DOWN = pygame.Vector2(0, 1)


class Probe(pygame.sprite.Sprite):
    FILENAME = "../images/shoot.png"

    SPEED = 100

    image: pygame.Surface
    rect: pygame.FRect

    @classmethod
    def load_resources(cls):
        cls._image = pygame.image.load(cls.FILENAME).convert_alpha()

    def __init__(self, viewport: pygame.Rect, center:tuple[int, int] = INITIAL_CENTER) -> None:
        super().__init__()

        self.image = Probe._image
        self.rect = pygame.FRect(self.image.get_rect())
        self.viewport = viewport

        self.radius = min(self.rect.width, self.rect.height) // 2  # see pygame.sprite.collide_circle()
        self.mask = pygame.mask.from_surface(self.image)  # see pygame.sprite.collide_mask()
        self.rect.center = center
        self.direction = Direction.STOP

    @override
    def update(self, dt: float) -> None:
        self.rect.move_ip(Probe.SPEED * self.direction.value * dt)
        self.rect.clamp_ip(self.viewport)

    def set_direction(self, direction: Direction) -> None:
        self.direction = direction
