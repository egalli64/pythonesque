"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

The need of having a break
"""
from typing import override

import pygame
from bullet import Bullet


class Enemy(pygame.sprite.Sprite):
    FILENAME = "../images/alien_big_1.png"

    MARGIN = 10
    SPEED = pygame.Vector2(150, 0)

    image: pygame.Surface = None
    rect: pygame.FRect = None

    @classmethod
    def load_resources(cls):
        cls._image = pygame.image.load(cls.FILENAME).convert_alpha()

    def __init__(self, viewport: pygame.Rect) -> None:
        super().__init__()

        self.image = Enemy._image
        self.rect: pygame.FRect = pygame.FRect(self.image.get_rect())
        self.rect.topleft = (viewport.left + Enemy.MARGIN, viewport.top + Enemy.MARGIN)
        self.viewport = viewport
        self.direction = 1  # right

    def fire(self) -> Bullet:
        pos = self.rect.move(0, 20).center
        return Bullet(pos, self.viewport.height)

    @override
    def update(self, dt: float) -> None:
        candidate = self.rect.move(Enemy.SPEED * dt * self.direction)
        if candidate.left < self.viewport.left + Enemy.MARGIN or candidate.right > self.viewport.right - Enemy.MARGIN:
            self.direction *= -1
        else:
            self.rect = candidate
