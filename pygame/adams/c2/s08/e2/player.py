"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Collision between a sprite and a group of sprites
"""
from enum import Enum
from typing import override

import pygame


class Direction(Enum):
    STOP = pygame.Vector2(0, 0)
    RIGHT = pygame.Vector2(1, 0)
    LEFT = pygame.Vector2(-1, 0)
    UP = pygame.Vector2(0, -1)
    DOWN = pygame.Vector2(0, 1)


class Player(pygame.sprite.Sprite):
    START_POS = (320, 240)
    SIZE = (40, 40)
    COLOR = (50, 200, 50)
    SPEED = 100

    image: pygame.Surface
    rect: pygame.FRect

    def __init__(self, viewport: pygame.Rect) -> None:
        super().__init__()

        self.viewport = viewport
        self.image = pygame.Surface(Player.SIZE)
        self.image.fill(Player.COLOR)
        self.rect = pygame.FRect(self.image.get_rect(center=Player.START_POS))
        self.direction = Direction.STOP

    def set_direction(self, direction: Direction) -> None:
        self.direction = direction

    @override
    def update(self, dt: float) -> None:
        self.rect.move_ip(Player.SPEED * self.direction.value * dt)
        self.rect.clamp_ip(self.viewport)
