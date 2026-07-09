"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Bubble game

Credits:
 * Fishtank image: https://www.pngwing.com/en/free-png-vadpk
 * Sound: https://www.fesliyanstudios.com/royalty-free-sound-effects-download
"""

from random import randint
from typing import Tuple

import pygame
from settings import Settings
from bubble_factory import BubbleFactory


class Bubble(pygame.sprite.Sprite):
    image: pygame.Surface
    rect: pygame.Rect

    def __init__(self, speed: int) -> None:
        """Constructor."""
        super().__init__()

        self.factory = BubbleFactory()

        self.radius: float = BubbleFactory.RADIUS_RANGE[0]
        self.image = self.factory.get(self.radius)

        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self, dt) -> None:
        self.radius += self.speed * dt
        self.radius = min(self.radius, BubbleFactory.RADIUS_RANGE[1])
        center = self.rect.center

        self.image = self.factory.get(self.radius)

        self.rect = self.image.get_rect()
        self.rect.center = center

    def offending(self) -> None:
        self.image = self.factory.get(self.radius, False)

    def randompos(self) -> None:
        """Computes a new position of the center by random."""
        distance = Settings.DISTANCE + BubbleFactory.RADIUS_RANGE[0]
        center_x = randint(
            Settings.PLAYGROUND.left + distance,
            Settings.PLAYGROUND.right - distance,
        )
        center_y = randint(
            Settings.PLAYGROUND.top + distance,
            Settings.PLAYGROUND.bottom - distance,
        )
        self.rect.center = (center_x, center_y)

    def pop(self):
        self.kill()
        return round(self.radius)

    def contains(self, pos: Tuple[int, int]) -> bool:
        delta_x = pos[0] - self.rect.centerx
        delta_y = pos[1] - self.rect.centery
        return delta_x * delta_x + delta_y * delta_y <= self.radius * self.radius
