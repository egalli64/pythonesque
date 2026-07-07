"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Bubble game

Credits:
 * Fishtank image: https://www.pngwing.com/en/free-png-vadpk
 * Sound: https://www.fesliyanstudios.com/royalty-free-sound-effects-download
"""

import pygame
from settings import Settings


class BubbleContainer:
    """A simple container class to manage the bubbles of different sizes."""

    def __init__(self, filename: str) -> None:
        """Constructor.

        Args:
            filename (str): Filename of the bubble picture file
        """
        imagename = Settings.get_image(filename)
        image: pygame.Surface = pygame.image.load(imagename).convert_alpha()
        self.images = {
            i: pygame.transform.scale(image, (i * 2, i * 2))
            for i in range(Settings.RADIUS["min"], Settings.RADIUS["max"] + 1)
        }

    def get(self, radius: int) -> pygame.Surface:
        """Gets the bubble image with the radius <radius>.

        Args:
            radius (int): radius of the bubble

        Returns:
            pygame.Surface: Scaled image of the bubble
        """
        radius = max(Settings.RADIUS["min"], radius)
        radius = min(Settings.RADIUS["max"], radius)
        return self.images[radius]
