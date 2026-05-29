"""
Python Crash Course, Third Edition, Part II https://nostarch.com/python-crash-course-3rd-edition
My notes: https://github.com/egalli64/pythonesque/ pygame/pcc3 folder

Chapter 12 - A Ship that fires bullets
Starting the Game Project
"""

import pygame

SHIP_IMAGE = "../../images/ship.bmp"


class Ship:
    """A class to manage the ship."""

    def __init__(self, screen):
        """Initialize the ship and set its starting position."""
        self.screen = screen

        # Load the ship image and get its rect.
        self.image = pygame.image.load(SHIP_IMAGE)
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = screen.get_rect().midbottom

    def blit(self):
        """Draw the ship at its current location in the injected screen"""
        self.screen.blit(self.image, self.rect)
