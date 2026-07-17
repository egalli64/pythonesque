"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Mouse actions
"""
from typing import override
import pygame


class Ball(pygame.sprite.Sprite):
    FILENAME = "../../images/blue_ball.png"
    MIN_SIZE = 10
    INITIAL_SIZE = 50
    MAX_SIZE = 400

    dirty: bool
    image: pygame.Surface
    rect: pygame.FRect

    def __init__(self, viewport) -> None:
        super().__init__()

        self.image_base = pygame.image.load(Ball.FILENAME).convert_alpha()
        self.size = Ball.INITIAL_SIZE
        self.image = self.scale()
        self.rect = pygame.FRect(self.image.get_rect())
        self.viewport = viewport

    def scale(self):
        self.dirty = False
        return pygame.transform.scale(self.image_base, (self.size, self.size))

    @override
    def update(self, pos) -> None:
        self.set_center(pos)
        self.rect.clamp_ip(self.viewport)
        if self.dirty:
            center = self.rect.center
            self.image = self.scale()
            self.rect = pygame.FRect(self.image.get_rect())
            self.rect.center = center

    def draw(self, screen: pygame.Surface) -> None:
        screen.blit(self.image, self.rect)

    def rotate(self, ccw: bool) -> None:
        self.dirty = True
        angle = 90 * (1 if ccw else -1)
        self.image_base = pygame.transform.rotate(self.image_base, angle)

    def resize(self, delta: int) -> None:
        if Ball.MIN_SIZE <= self.size + delta <= Ball.MAX_SIZE:
            self.size += delta
            self.dirty = True

    def set_center(self, center: tuple[int, int]) -> None:
        self.rect.center = center
