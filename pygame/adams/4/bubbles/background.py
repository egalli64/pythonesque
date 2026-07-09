"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Bubble game

Credits:
 * Fishtank image: https://www.pngwing.com/en/free-png-vadpk
 * Sound: https://www.fesliyanstudios.com/royalty-free-sound-effects-download
"""

import pygame


class Background:
    FILENAME = "images/aquarium.png"

    @classmethod
    def load_resources(cls):
        cls._image = pygame.image.load(Background.FILENAME).convert()

    def __init__(self, viewport) -> None:
        self.image: pygame.Surface = Background._image
        self.image = pygame.transform.scale(self.image, viewport.size)
        self.rect = self.image.get_rect()

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        pygame.draw.rect(screen, (255, 0, 0), (90, 90, 1055, 615), 1)
