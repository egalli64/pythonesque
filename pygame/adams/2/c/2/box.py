"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

User defined events
"""
import pygame
from typing import override

EVENT_OVERFLOW = pygame.event.custom_type()


class Box(pygame.sprite.Sprite):
    IMAGE_SIZE = (50, 20)
    BACKGROUND_COLOR = "gray"
    FONT_SIZE = 30
    TEXT_COLOR = "blue"
    TEXT_POS = (18, 1)

    image: pygame.Surface

    @classmethod
    def load_resources(cls) -> None:
        cls._font = pygame.font.SysFont(None, cls.FONT_SIZE)

    def __init__(self, index: int, viewport: pygame.Rect) -> None:
        super().__init__()
        self.image = pygame.Surface(Box.IMAGE_SIZE)
        pos = (viewport.right - 50 - index * 100, viewport.centery)
        self.rect = self.image.get_rect(center=pos)
        self.value = 0
        self.index = index
        self.dirty = True

    @override
    def update(self) -> None:
        if self.dirty:
            self.image.fill(Box.BACKGROUND_COLOR)
            text = Box._font.render(f"{self.value}", False, Box.TEXT_COLOR)
            self.image.blit(text, Box.TEXT_POS)
            self.dirty = False

    def increase(self, delta: int) -> None:
        current = self.value + delta
        self.value = current % 10
        if x := current // 10:
            event = pygame.event.Event(EVENT_OVERFLOW, next=self.index + 1, delta=x)
            pygame.event.post(event)
        self.dirty = True
