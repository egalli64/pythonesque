"""
Python Crash Course, Third Edition, Part II https://nostarch.com/python-crash-course-3rd-edition
My notes: https://github.com/egalli64/pythonesque/ pygame/pcc3 folder

Chapter 14 - Scoring
Adding the play button
"""

BULLET_SPEED = 2
BULLET_WIDTH = 3
BULLET_HEIGHT = 15
BULLET_COLOR = (60, 60, 60)
BULLETS_ALLOWED = 3

import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class to manage bullets fired from the ship."""

    rect: pygame.Rect

    def __init__(self, screen, ship_rect):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = screen
        self.color = BULLET_COLOR

        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, BULLET_WIDTH, BULLET_HEIGHT)  # type: ignore
        self.rect.midtop = ship_rect.midtop

        # Store the bullet's position as a float.
        self.y = float(self.rect.y)

    def update(self):
        """
        Move the bullet up the screen

        Autoremove when exit the screen
        """
        # Update the exact position of the bullet.
        self.y -= BULLET_SPEED
        # Update the rect position.
        self.rect.y = self.y
        if self.rect.y < 0:
            self.kill()

    def draw(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
