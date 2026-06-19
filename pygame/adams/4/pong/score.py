"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Pong score
"""

import pygame
from settings import Settings


class Score(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.font = pygame.font.SysFont(None, 30)
        self.score = {1: 0, 2: 0}
        self.image: pygame.Surface | None = None
        self.rect: pygame.Rect | None = None
        self.render()

    def update(self, *args, **kwargs) -> None:
        if "player" in kwargs.keys():
            self.score[kwargs["player"]] += 1
            self.render()
        return super().update(*args, **kwargs)

    def render(self):
        """Renders the score."""
        self.image = self.font.render(
            f"{self.score[1]} : {self.score[2]}", True, "white"
        )
        self.rect = self.image.get_rect(centerx=Settings.WINDOW.centerx, top=15)
