"""
Python Crash Course, Third Edition, Part II https://nostarch.com/python-crash-course-3rd-edition
My version: https://github.com/egalli64/pythonesque/ pygame/pcc3 folder
"""

from typing import override

import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """A class to manage the ship."""

    rect: pygame.Rect

    DEFAULT_SPEED = 10.0
    IMAGE = "images/ship.bmp"

    def __init__(self, screen):
        """
        Load the ship image and gets its rect.

        Define as helpers the ship rightmost and starting position.
        The initialization is completed by setup()

        screen: the game screen
        """
        super().__init__()

        self.screen = screen
        self.image = pygame.image.load(Ship.IMAGE)
        self.rect = self.image.get_rect()  # type: ignore
        self.MAX_X = self.screen.get_rect()[2] - self.rect[2]
        self.START_POS = self.screen.get_rect().midbottom
        self.speed = Ship.DEFAULT_SPEED

        self.setup()

    def setup(self, reset_speed=False):
        """
        Complete the setup / reset the ship its initial status.

        Define / reset the movement flags (left and right) and position (x also as float).

        reset_speed: True to get a speed reset to its default value
        """
        self.moving_left = False
        self.moving_right = False

        if reset_speed:
            self.speed = Ship.DEFAULT_SPEED

        self.rect.midbottom = self.START_POS
        self.x = float(self.rect.x)

    @override
    def update(self):
        """Update the ship's position based on the movement flag, clamping x in the expected area."""
        if self.moving_right:
            self.x += self.speed
        if self.moving_left:
            self.x -= self.speed

        self.x = max(min(self.x, self.MAX_X), 0)
        self.rect.x = self.x

    def blit(self):
        """Draw the ship at its current location in the injected screen"""
        self.screen.blit(self.image, self.rect)
