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
    INITIAL_SIZE_RATIO = 5

    image: pygame.Surface
    rect: pygame.FRect
    dirty: bool

    @classmethod
    def load_resources(cls) -> None:
        cls._image = pygame.image.load(cls.FILENAME).convert_alpha()

    def __init__(self, viewport: pygame.Rect) -> None:
        assert viewport.width == viewport.height, "Squared viewport expected"
        super().__init__()

        self.size = viewport.width / Ball.INITIAL_SIZE_RATIO
        self.viewport = viewport
        self.reset()
        self.rect.center = viewport.center

    def reset(self) -> None:
        self.image = pygame.transform.scale(Ball._image, (self.size, self.size))
        self.rect = pygame.FRect(self.image.get_rect())
        self.dirty = False

    @override
    def update(self, pos: tuple[int, int]) -> None:
        if self.dirty:
            self.reset()
        if self.rect.center != pos:
            self.rect.center = pos
            self.rect.clamp_ip(self.viewport)

    def rotate(self, counterclockwise: bool) -> None:
        self.dirty = True
        angle = 90 * (1 if counterclockwise else -1)
        Ball._image = pygame.transform.rotate(Ball._image, angle)

    def resize(self, delta: int) -> None:
        candidate = self.size + delta
        if Ball.MIN_SIZE <= candidate <= self.viewport.width:
            self.size = candidate
            self.dirty = True
