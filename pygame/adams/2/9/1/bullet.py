"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

The need of having a break
"""
from typing import Tuple, override
import pygame


class Bullet(pygame.sprite.Sprite):
    # MAX_Y = WIN_RECT.bottom - 30
    Y_GAP = 30

    image: pygame.Surface
    rect: pygame.FRect

    def __init__(self, filename: str, pos: Tuple, viewport_height: int) -> None:
        super().__init__()
        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = pygame.FRect(self.image.get_rect())
        self.rect.center = pos
        self.direction = 1
        self.speed = pygame.math.Vector2(0, 100)
        self.viewport_height = viewport_height

    @override
    def update(self, dt) -> None:
        self.rect.move_ip(self.speed * dt * self.direction)
        if self.rect.top > self.viewport_height - Bullet.Y_GAP:
            self.kill()
