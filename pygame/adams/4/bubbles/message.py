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


class Message(pygame.sprite.Sprite):
    """Draws a shadow and a text in the foreground of the game."""

    def __init__(self, filename: str) -> None:
        super().__init__()
        imagename = Settings.get_image(filename)
        self.image: pygame.Surface = pygame.image.load(imagename).convert_alpha()
        self.rect = self.image.get_rect()
