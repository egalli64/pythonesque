"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

A running cat - dt from main loop
"""
from typing import override
import pygame
from animation import Animation


class Cat(pygame.sprite.Sprite):
    FILE_TEMPLATE = "../../images/cat-{:d}.bmp"
    TRANSPARENT_COLOR = "black"

    def __init__(self, viewport: pygame.Rect) -> None:
        super().__init__()
        filenames = [Cat.FILE_TEMPLATE.format(i) for i in range(6)]
        self.animation = Animation(filenames, Cat.TRANSPARENT_COLOR)

        self.image: pygame.Surface = self.animation.image
        self.rect: pygame.Rect = self.image.get_rect()
        self.rect.center = viewport.center

    @override
    def update(self, dt) -> None:
        self.animation.update(dt)
        self.image = self.animation.image
