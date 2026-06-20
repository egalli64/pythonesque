"""
Master Python by making 5 games - 1: Space shooter

YouTube: https://www.youtube.com/watch?v=8OMghdHP-zs
GitHub: https://github.com/clear-code-projects/5games/tree/main/space%20shooter
Drive: https://drive.google.com/drive/folders/1bUGO9sv5SM3gYO_t9zgifedkQKHUYudO

My version: https://github.com/egalli64/pythonesque/ pygame/clear-code folder
"""

from random import randint
import pygame


class Star(pygame.sprite.Sprite):
    FILENAME = "images/star.png"
    _image: pygame.Surface

    @classmethod
    def load_resources(cls):
        cls._image = pygame.image.load(Star.FILENAME).convert_alpha()

    @classmethod
    def create_field(cls, n: int, rect: pygame.Rect, group: pygame.sprite.Group):
        for _ in range(n):
            Star(*rect.size, group)

    def __init__(self, width, height, group):
        super().__init__(group)
        self.image = Star._image
        center = (randint(0, width), randint(0, height))
        self.rect = Star._image.get_rect(center=center)
