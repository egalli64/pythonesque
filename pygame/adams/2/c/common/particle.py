"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

User defined events
"""
import pygame
from random import choice, randint
from typing import override

SPEED_INTERVAL = (50, 100)
SIZE_INTERVAL = (3, 6)
GREEN_INTERVAL = (100, 255)


class Particle(pygame.sprite.Sprite):
    image: pygame.Surface
    rect: pygame.Rect

    def __init__(self, viewport: pygame.Rect, group, frozen=True) -> None:
        super().__init__(group)

        self.image = pygame.Surface((randint(*SIZE_INTERVAL), randint(*SIZE_INTERVAL)))
        self.image.fill((0, randint(*GREEN_INTERVAL), 0))
        self.rect: pygame.FRect = pygame.FRect(self.image.get_rect())
        self.rect.topleft = (randint(30, viewport.right - 30), randint(30, viewport.bottom - 30))

        self.viewport = viewport
        self.speed = randint(*SPEED_INTERVAL)
        self.direction = pygame.Vector2(choice((-1, 1)), choice((-1, 1)))
        self.frozen = frozen

    @override
    def update(self, td) -> None:
        if not self.frozen:
            self.rect.move_ip(self.speed * self.direction * td)
            if self.rect.left < 0 or self.rect.right > self.viewport.right:
                self.direction[0] *= -1
            if self.rect.top < 0 or self.rect.bottom > self.viewport.bottom:
                self.direction[1] *= -1
            self.rect.clamp_ip(self.viewport)

    def set_frozen(self, frozen: bool):
        self.frozen = frozen
