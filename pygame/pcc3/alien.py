"""
Python Crash Course, Third Edition, Part II https://nostarch.com/python-crash-course-3rd-edition
My version: https://github.com/egalli64/pythonesque/ pygame/pcc3 folder
"""

import pygame

from pygame.sprite import Sprite


class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    rect: pygame.Rect
    DEFAULT_SPEED = 1.0
    IMAGE = "images/alien.bmp"

    fleet_direction = 1
    speed = DEFAULT_SPEED

    def __init__(self, screen):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = screen

        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load(Alien.IMAGE)
        self.rect = self.image.get_rect()  # type: ignore

        # leave one alien size free on top and on left
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x)

    def update(self):
        """Move the alien to the right."""
        self.x += Alien.speed * Alien.fleet_direction
        self.rect.x = self.x

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)
