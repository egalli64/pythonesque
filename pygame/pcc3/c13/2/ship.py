"""
Python Crash Course, Third Edition, Part II https://nostarch.com/python-crash-course-3rd-edition
My notes: https://github.com/egalli64/pythonesque/ pygame/pcc3 folder

Chapter 13 - Aliens!
Making the Fleet Move
"""

import pygame

DEFAULT_SHIP_SPEED = 10
SHIP_IMAGE = "../../images/ship.bmp"


class Ship:
    """A class to manage the ship."""

    def __init__(self, screen):
        """Initialize the ship and set its starting position."""
        self.screen = screen

        # Load the ship image and get its rect.
        self.image = pygame.image.load(SHIP_IMAGE)
        self.rect = self.image.get_rect()
        # sheep rightmost x position
        self.max_x = screen.get_rect()[2] - self.rect[2]

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = screen.get_rect().midbottom

        # Movement flags; start with a ship that's not moving.
        self.moving_right = False
        self.moving_left = False

        self.ship_speed = DEFAULT_SHIP_SPEED

    def update(self):
        """Update the ship's position based on the movement flag."""
        if self.moving_right:
            self.rect.x += self.ship_speed
        if self.moving_left:
            self.rect.x -= self.ship_speed

        # clamp x to the screen
        self.rect.x = max(min(self.rect.x, self.max_x), 0)

    def blit(self):
        """Draw the ship at its current location in the injected screen"""
        self.screen.blit(self.image, self.rect)
