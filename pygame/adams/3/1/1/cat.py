"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

A running cat
"""
from typing import override
import pygame
from animation import Animation


class Cat(pygame.sprite.Sprite):
    FILE_TEMPLATE = "../../images/cat-{:d}.bmp"
    TRANSPARENT_COLOR = "black"

    image: pygame.Surface
    rect: pygame.Rect

    def __init__(self, viewport: pygame.Rect) -> None:
        super().__init__()
        self.animation = Animation([Cat.FILE_TEMPLATE.format(i) for i in range(6)])

        self.image = self.animation.current()
        self.rect = self.image.get_rect(center=viewport.center)

    @override
    def update(self) -> None:
        self.image = self.animation.current()

    def change_timing(self, delta: int) -> None:
        self.animation.change_timing(delta)
