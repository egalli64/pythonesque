"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Exploding rocks
"""
import random
import pygame
from explosion import Explosion
from timer import Timer


class Rock(pygame.sprite.Sprite):
    FILENAME = "../../images/rock.png"
    LIFE_SPAN_INTERVAL = (100, 2000)

    @classmethod
    def load_resources(cls) -> None:
        cls._image = pygame.image.load(Rock.FILENAME).convert_alpha()

    image: pygame.Surface
    rect: pygame.Rect

    def __init__(self, viewport: pygame.Rect):
        super().__init__()

        self.image = Rock._image
        width, height = self.image.get_size()
        bottom_right = (random.randint(width, viewport.width), random.randint(height, viewport.height))
        self.rect = self.image.get_rect(bottomright=bottom_right)

        self.animation = Explosion()
        self.timer = Timer(random.randint(*Rock.LIFE_SPAN_INTERVAL))
        self.explosion = False

    def update(self) -> None:
        if self.timer.tick():
            self.explosion = True
        if self.explosion:
            self.image = self.animation.current()
            self.rect = self.image.get_rect(center=self.rect.center)
        if self.animation.done():
            self.kill()
