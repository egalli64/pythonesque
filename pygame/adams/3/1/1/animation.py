"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

A running cat
"""
import pygame
from timer import Timer


class Animation:
    def __init__(self, namelist: list[str], delta: int = 100, colorkey="black") -> None:
        self.images: list[pygame.Surface] = []
        self.timer = Timer(delta)
        for filename in namelist:
            bitmap = pygame.image.load(filename).convert()
            bitmap.set_colorkey(colorkey)
            self.images.append(bitmap)
        self.index = 0

    def current(self) -> pygame.Surface:
        if self.timer.tick():
            self.index = (self.index + 1) % len(self.images)
        return self.images[self.index]

    def change_timing(self, delta: int) -> None:
        self.timer.change_duration(delta)
