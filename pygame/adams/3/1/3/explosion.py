"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Colliding rocks
"""
import pygame
from timer import Timer


class Explosion:
    EXPLOSION_TEMPLATE = "../../images/explosion-{:d}.png"
    DELTA_TIME = 100

    @classmethod
    def load_resources(cls) -> None:
        cls._images: list[pygame.Surface] = []

        filenames = [cls.EXPLOSION_TEMPLATE.format(i) for i in range(1, 5)]
        for filename in filenames:
            bitmap = pygame.image.load(filename).convert_alpha()
            cls._images.append(bitmap)

    def __init__(self) -> None:
        self.timer = Timer(Explosion.DELTA_TIME)
        self.index = 0
        self.running = True

    def current(self) -> pygame.Surface:
        if self.timer.tick():
            if self.index < len(Explosion._images) - 1:
                self.index += 1
            else:
                self.running = False
        return Explosion._images[self.index]

    def done(self) -> bool:
        return not self.running
