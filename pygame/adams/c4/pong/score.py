"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Pong score
"""
from typing import override

import pygame


class Score(pygame.sprite.Sprite):
    CENTER_X = 500
    TOP = 15
    TEXT = "{} : {}"
    COLOR = "white"

    image: pygame.Surface
    rect: pygame.Rect

    def __init__(self, *groups):
        super().__init__(*groups)
        self.font = pygame.font.SysFont(None, 36)
        self.score = {1: 0, 2: 0}

    def point_for(self, player):
        self.score[player] += 1

    @override
    def update(self, *args, **kwargs):
        text = Score.TEXT.format(self.score[1], self.score[2])
        self.image = self.font.render(text, True, Score.COLOR)
        self.rect = self.image.get_rect(centerx=Score.CENTER_X, top=Score.TOP)
