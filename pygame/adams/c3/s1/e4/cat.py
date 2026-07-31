"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

A running cat - dt from main loop
"""
from typing import override
import pygame

MIN_DURATION = 0.01
DEFAULT_DURATION_TIME = 0.1
FILE_TEMPLATE = "../../images/cat-{:d}.bmp"
TRANSPARENT_COLOR = "black"


class Cat(pygame.sprite.Sprite):
    image: pygame.Surface
    rect: pygame.Rect

    @classmethod
    def load_resources(cls) -> None:
        filenames = [FILE_TEMPLATE.format(i) for i in range(6)]
        cls._images = []
        for filename in filenames:
            bitmap = pygame.image.load(filename).convert()
            bitmap.set_colorkey(TRANSPARENT_COLOR)
            cls._images.append(bitmap)

    def __init__(self, viewport: pygame.Rect) -> None:
        super().__init__()

        self.duration = DEFAULT_DURATION_TIME
        self.timer = 0.0
        self.index = 0

        self.image = Cat._images[self.index]
        self.rect = self.image.get_rect(center=viewport.center)

    @override
    def update(self, dt) -> None:
        self.timer += dt

        next_frame = False
        while self.timer >= self.duration:
            self.timer -= self.duration
            self.index = (self.index + 1) % len(Cat._images)
            next_frame = True

        if next_frame:
            self.image = Cat._images[self.index]

    def change_duration(self, increase: bool):
        delta = MIN_DURATION * (1 if increase else -1)
        self.duration = max(MIN_DURATION, self.duration + delta)
