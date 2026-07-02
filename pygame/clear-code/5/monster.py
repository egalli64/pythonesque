"""
Master Python by making 5 games - 5: Monster battle

YouTube: https://www.youtube.com/watch?v=8OMghdHP-zs&t=32960s
GitHub: https://github.com/clear-code-projects/5games/tree/main/Monster%20battle
Google Drive: https://drive.google.com/drive/folders/15VQ37pgCwXxHZ8oBK0yc_CzKQeP2qSSl

My version: https://github.com/egalli64/pythonesque/ pygame/clear-code folder
"""

import pygame

from settings import MONSTER_DATA, ABILITIES_DATA, WINDOW_HEIGHT, WINDOW_WIDTH
from random import sample


class Creature:
    def get_data(self, name):
        self.element = MONSTER_DATA[name]["element"]
        self._health = self.max_health = MONSTER_DATA[name]["health"]
        self.abilities = sample(list(ABILITIES_DATA.keys()), 4)
        self.name = name

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        self._health = min(self.max_health, max(0, value))


class Monster(pygame.sprite.Sprite, Creature):
    def __init__(self, name, surf):
        super().__init__()
        self.image = surf
        self.rect = self.image.get_frect(bottomleft=(100, WINDOW_HEIGHT))
        self.get_data(name)

    def __repr__(self):
        return f"{self.name}: {self.health}/{self.max_health}"


class Opponent(pygame.sprite.Sprite, Creature):
    def __init__(self, name, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(midbottom=(WINDOW_WIDTH - 250, 300))
        self.get_data(name)
