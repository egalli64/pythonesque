"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

The need of having a break
"""
from typing import override

import pygame
from bullet import Bullet

WIN_RECT = pygame.Rect(0, 0, 700, 200)
FPS = 30
TITLE = "Bugged continuous fire"


class Enemy(pygame.sprite.Sprite):
    FILENAME = "../../images/alien_big_1.png"

    MIN_X = 10
    MAX_X = WIN_RECT.right - 10
    START_POS = (MIN_X, 10)
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
        self.rect.topleft = Enemy.START_POS
        self.viewport = viewport
        self.direction = 1  # right

    def fire(self) -> Bullet:
        pos = self.rect.move(0, 20).center
        return Bullet(pos, self.viewport.height)

    @override
    def update(self, dt) -> None:
        candidate = self.rect.move(Enemy.SPEED * dt * self.direction)
        if candidate.left < self.MIN_X or candidate.right > self.MAX_X:
            self.direction *= -1
        else:
            self.rect = candidate
