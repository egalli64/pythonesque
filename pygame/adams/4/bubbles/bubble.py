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

        self.mode = "blue"
        self.radius = BubbleFactory.RADIUS_RANGE[0]

        plain = self.mode == "blue"
        self.image = self.factory.get(plain, self.radius)

        self.rect = self.image.get_rect()
        self.fradius = float(self.radius)
        self.speed = speed

    def update(self, *args, **kwargs) -> None:
        """Let the bubble grow.

        Args:
            *args (Tuple[int]): not used
            **kwargs Dict[str, Any]: possible key/value pairs:
                                      (action/grow), (action/sting),
                                      (mode/blue), (mode/red))
        """
        if "action" in kwargs.keys():
            dt = 1 / 60  # TODO: use actual dt
            if kwargs["action"] == "grow":
                self.fradius += self.speed * dt
                self.fradius = min(self.fradius, BubbleFactory.RADIUS_RANGE[1])
                self.radius = round(self.fradius)
                center = self.rect.center

                plain = self.mode == "blue"
                self.image = self.factory.get(plain, self.radius)

                self.rect = self.image.get_rect()
                self.rect.center = center
        elif "mode" in kwargs.keys():
            self.set_mode(kwargs["mode"])

    def set_mode(self, mode: str) -> None:
        """Sets the bubble in the mode "red" or "blue".

        Args:
            mode (str): "red" oder "blue"
        """
        if mode != self.mode:
            self.mode = mode

            plain = self.mode == "blue"
            self.image = self.factory.get(plain, self.radius)

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

    def sting(self):
        self.kill()
        return self.radius

    def contains(self, pos: Tuple[int, int]) -> bool:
        delta_x = pos[0] - self.rect.centerx
        delta_y = pos[1] - self.rect.centery
        return delta_x * delta_x + delta_y * delta_y <= self.radius * self.radius
