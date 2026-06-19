"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Pong pause
"""

import pygame
from typing import Tuple
from settings import Settings


class Pause(pygame.sprite.Sprite):
    def __init__(self, *groups: Tuple[pygame.sprite.Group]) -> None:
        super().__init__(*groups)
        self.rect = pygame.Rect(Settings.WINDOW.topleft, Settings.WINDOW.size)
        self.image = pygame.Surface(self.rect.size).convert_alpha()
        self.image.fill([120, 120, 120, 200])
