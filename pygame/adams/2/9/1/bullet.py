"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

The need of having a break
"""
from typing import override
import pygame


class Bullet(pygame.sprite.Sprite):
    FILENAME = "../../images/shoot.png"
    SPEED = 100
    Y_GAP = 30

    image: pygame.Surface
    rect: pygame.FRect

    @classmethod
    def load_resources(cls):
        cls._image = pygame.image.load(cls.FILENAME).convert_alpha()

    def __init__(self, pos: tuple[float, float], viewport_height: int) -> None:
        super().__init__()

        self.image = Bullet._image
        self.rect = pygame.FRect(self.image.get_rect())
        self.rect.center = pos
        self.viewport_height = viewport_height

    @override
    def update(self, dt: float) -> None:
        self.rect.y += Bullet.SPEED * dt
        if self.rect.top > self.viewport_height - Bullet.Y_GAP:
            self.kill()
