"""
Python Crash Course, Third Edition, Part II https://nostarch.com/python-crash-course-3rd-edition
My notes: https://github.com/egalli64/pythonesque/ pygame/pcc3 folder

Chapter 14 - Scoring
Leveling up
"""

import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class to manage bullets fired from the ship."""

    WIDTH = 3
    HEIGHT = 15
    COLOR = (60, 60, 60)

    rect: pygame.Rect

    def __init__(self, screen, ship_rect, speed):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = screen
        self.color = Bullet.COLOR

        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, Bullet.WIDTH, Bullet.HEIGHT)  # type: ignore
        self.rect.midtop = ship_rect.midtop

        # Store the bullet's position as a float.
        self.speed = speed
        self.y = float(self.rect.y)

    def update(self):
        """
        Move the bullet up the screen

        Autoremove when exit the screen
        """
        # Update the exact position of the bullet.
        self.y -= self.speed
        # Update the rect position.
        self.rect.y = self.y
        if self.rect.y < 0:
            self.kill()

    def draw(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
