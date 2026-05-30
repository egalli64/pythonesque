"""
Python Crash Course, Third Edition, Part II https://nostarch.com/python-crash-course-3rd-edition
My notes: https://github.com/egalli64/pythonesque/ pygame/pcc3 folder

Chapter 13 - Aliens!
Building the alien fleet
"""

import pygame

from pygame.sprite import Sprite

ALIEN_IMAGE = "../../images/alien.bmp"


class Alien(Sprite):
    """A class to represent a single alien in the fleet."""
    rect: pygame.Rect

    def __init__(self, screen):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = screen

        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load(ALIEN_IMAGE)
        self.rect = self.image.get_rect() # type: ignore

        # leave one alien size free on top and on left
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x)
