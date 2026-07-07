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


class Background(pygame.sprite.Sprite):
    """Sprite class with nearly no function for drawing the background image."""

    def __init__(self, viewport) -> None:
        super().__init__()
        imagename = Settings.get_image("aquarium.png")
        self.image: pygame.Surface = pygame.image.load(imagename).convert()
        self.image = pygame.transform.scale(self.image, viewport.size)
        self.rect = self.image.get_rect()
