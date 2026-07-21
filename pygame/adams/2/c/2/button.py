"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

User defined events
"""
import pygame
from typing import override

EVENT_BUTTON_PRESSED = pygame.event.custom_type()


class StartButton(pygame.sprite.Sprite):
    TEXT_COLOR = "black"
    TEXT = ("Stop", "Start")

    image: pygame.Surface
    rect: pygame.Rect

    def __init__(self, pos, group) -> None:
        super().__init__(group)
        self.font = pygame.font.SysFont(None, 30)
        self.running = False
        self.image = self.font.render(StartButton.TEXT[1], True, StartButton.TEXT_COLOR)
        self.rect = self.image.get_rect(topleft=pos)
        self.dirty = False

    @override
    def update(self) -> None:
        if self.dirty:
            text = StartButton.TEXT[0] if self.running else StartButton.TEXT[1]
            self.image = self.font.render(text, True, StartButton.TEXT_COLOR)
            self.dirty = False

    def on_click(self, pos: tuple[int, int]) -> None:
        if self.rect.collidepoint(pos):
            event_out = pygame.event.Event(EVENT_BUTTON_PRESSED, running=self.running)
            pygame.event.post(event_out)

            self.running = not self.running
            self.dirty = True
