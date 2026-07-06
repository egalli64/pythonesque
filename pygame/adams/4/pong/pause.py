"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Pong pause
"""

import pygame


class Pause:
    def __init__(self, viewport):
        self.rect = pygame.Rect(viewport.topleft, viewport.size)
        self.image = pygame.Surface(self.rect.size).convert_alpha()
        self.image.fill([120, 120, 120, 200])

    def draw(self, screen):
        screen.blit(self.image, self.rect)
