"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

User defined events
"""
from typing import override
import pygame
from common.custom_event import CustomEvent


class StartButton(pygame.sprite.Sprite):
    TEXT_COLOR = "black"
    BORDER_COLOR = "blue"
    TEXT = ("Stop", "Start")
    FONT_SIZE = 30

    image: pygame.Surface
    rect: pygame.Rect

    @classmethod
    def load_resources(cls) -> None:
        cls._font = pygame.font.Font(None, cls.FONT_SIZE)

    def __init__(self, pos, group) -> None:
        super().__init__(group)

        self.running = False
        self.rect = pygame.Rect(pos, (0, 0))
        self.dirty = True

    @override
    def update(self) -> None:
        if self.dirty:
            text = StartButton.TEXT[0] if self.running else StartButton.TEXT[1]
            self.image = self._font.render(text, True, StartButton.TEXT_COLOR)
            pygame.draw.rect(self.image, StartButton.BORDER_COLOR, self.image.get_rect(), 1)
            self.rect.size = self.image.get_size()
            self.dirty = False

    def on_click(self, pos: tuple[int, int]) -> None:
        if self.rect.collidepoint(pos):
            self.toggle_running()

    def toggle_running(self) -> None:
        event_out = pygame.event.Event(CustomEvent.BUTTON_PRESSED, running=self.running)
        pygame.event.post(event_out)

        self.running = not self.running
        self.dirty = True
