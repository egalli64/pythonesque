"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Exploding rocks
"""
import random
import pygame
from animation import Animation
from timer import Timer


class Rock(pygame.sprite.Sprite):
    FILENAME = "../../images/rock.png"
    EXPLOSION_TEMPLATE = "../../images/explosion-{:d}.png"

    def __init__(self, viewport: pygame.Rect):
        super().__init__()
        self.image = pygame.image.load(Rock.FILENAME).convert_alpha()
        self.rect: pygame.Rect = self.image.get_rect()
        max_pos = (viewport.width - self.rect.width, viewport.height - self.rect.height)
        self.rect.centerx = random.randint(self.rect.width, max_pos[0])
        self.rect.centery = random.randint(self.rect.height, max_pos[1])
        explosions = [Rock.EXPLOSION_TEMPLATE.format(i) for i in range(1, 5)]
        self.animation = Animation(explosions, 100)
        self.timer = Timer(random.randint(100, 2000))
        self.explosion = False

    def update(self) -> None:
        if self.timer.tick():
            self.explosion = True
        if self.explosion:
            self.image = self.animation.current()
            center = self.rect.center
            self.rect = self.image.get_rect()
            self.rect.center = center
        if self.animation.done():
            self.kill()
