"""
Python Crash Course, Third Edition, Part II https://nostarch.com/python-crash-course-3rd-edition
My notes: https://github.com/egalli64/pythonesque/ pygame/pcc3 folder

Chapter 14 - Scoring
Scoring
"""

import pygame


class Ship:
    """A class to manage the ship."""

    DEFAULT_SPEED = 10.0
    IMAGE = "../../images/ship.bmp"

    def __init__(self, screen):
        """Initialize the ship and set its starting position."""
        self.screen = screen

        # Load the ship image and get its rect.
        self.image = pygame.image.load(Ship.IMAGE)
        self.rect = self.image.get_rect()
        # sheep rightmost position
        self.MAX_X = screen.get_rect()[2] - self.rect[2]
        # each new ship at the bottom center of the screen
        self.START_POS = screen.get_rect().midbottom

        self.setup()

    def setup(self):
        """Any time a new fleet is ready to invade"""
        # Movement flags; start with a ship that's not moving.
        self.moving_right = False
        self.moving_left = False

        self.speed = Ship.DEFAULT_SPEED

        self.rect.midbottom = self.START_POS
        self.x = float(self.rect.x)

    def update(self):
        """Update the ship's position based on the movement flag."""
        if self.moving_right:
            self.x += self.speed
        if self.moving_left:
            self.x -= self.speed

        # clamp x to the screen
        self.x = max(min(self.x, self.MAX_X), 0)

        # Update rect object from self.x.
        self.rect.x = self.x

    def blit(self):
        """Draw the ship at its current location in the injected screen"""
        self.screen.blit(self.image, self.rect)
