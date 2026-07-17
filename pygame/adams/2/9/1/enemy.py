"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

The need of having a break
"""
from typing import Tuple, override
import pygame

WIN_RECT = pygame.Rect(0, 0, 700, 200)
FPS = 30
TITLE = "Bugged continuous fire"


class Enemy(pygame.sprite.Sprite):
    MIN_X = 10
    MAX_X = WIN_RECT.right - 10
    START_POS = (MIN_X, 10)
    SPEED = pygame.Vector2(150, 0)

    def __init__(self, filename: str) -> None:
        super().__init__()
        self.image = pygame.image.load(filename).convert_alpha()
        self.rect: pygame.FRect = pygame.FRect(self.image.get_rect())
        self.rect.topleft = Enemy.START_POS
        self.direction = 1  # right

    def update(self, dt) -> None:
        newpos = self.rect.move(Enemy.SPEED * dt * self.direction)
        if newpos.left < self.MIN_X or newpos.right > self.MAX_X:
            self.direction *= -1
        else:
            self.rect = newpos
