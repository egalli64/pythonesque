"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Exploding rocks
"""
import pygame
from timer import Timer


class Explosion:
    def __init__(self, namelist: list[str], delta: int) -> None:
        self.images: list[pygame.Surface] = []
        self.timer = Timer(delta)
        for filename in namelist:
            bitmap = pygame.image.load(filename).convert_alpha()
            self.images.append(bitmap)
        self.index = 0
        self.running = True

    def current(self) -> pygame.Surface:
        if self.timer.tick():
            if self.index < len(self.images) - 1:
                self.index += 1
            else:
                self.running = False
        return self.images[self.index]

    def done(self) -> bool:
        return not self.running
