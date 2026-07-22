"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

A running cat
"""
from typing import override
import pygame
from timer import Timer


class Cat(pygame.sprite.Sprite):
    FILE_TEMPLATE = "../../images/cat-{:d}.bmp"
    DEFAULT_TIMING = 100
    TRANSPARENT_COLOR = "black"

    _images: list[pygame.Surface]
    image: pygame.Surface
    rect: pygame.Rect

    @classmethod
    def load_resources(cls) -> None:
        namelist = [Cat.FILE_TEMPLATE.format(i) for i in range(6)]
        cls._images = []
        for filename in namelist:
            bitmap = pygame.image.load(filename).convert()
            bitmap.set_colorkey(Cat.TRANSPARENT_COLOR)
            cls._images.append(bitmap)

    def __init__(self, viewport: pygame.Rect) -> None:
        super().__init__()

        self.timer = Timer(Cat.DEFAULT_TIMING)
        self.index = 0
        self.image = Cat._images[self.index]
        self.rect = self.image.get_rect(center=viewport.center)

    @override
    def update(self) -> None:
        if self.timer.tick():
            self.index = (self.index + 1) % len(Cat._images)
            self.image = Cat._images[self.index]

    def change_timing(self, delta: int) -> None:
        self.timer.change_duration(delta)
