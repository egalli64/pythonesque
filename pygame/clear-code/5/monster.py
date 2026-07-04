"""
Master Python by making 5 games - 5: Monster battle

YouTube: https://www.youtube.com/watch?v=8OMghdHP-zs&t=32960s
GitHub: https://github.com/clear-code-projects/5games/tree/main/Monster%20battle
Google Drive: https://drive.google.com/drive/folders/15VQ37pgCwXxHZ8oBK0yc_CzKQeP2qSSl

My version: https://github.com/egalli64/pythonesque/ pygame/clear-code folder
"""

from os.path import join
from os import walk
from random import sample
import pygame

from settings import MONSTER_DATA, ABILITIES_DATA, WINDOW_HEIGHT, WINDOW_WIDTH
from support import import_folder


class Creature(pygame.sprite.Sprite):
    PATH_BACK = "images/back"
    PATH_FRONT = "images/front"

    @classmethod
    def load_resources(cls):
        cls._backs = import_folder(cls.PATH_BACK)
        cls._fronts = import_folder(cls.PATH_FRONT)

    def __init__(self, name, *groups):
        super().__init__(*groups)

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


class Monster(Creature):
    BOTTOM_LEFT = (100, WINDOW_HEIGHT)

    def __init__(self, name):
        super().__init__(name)
        self.image: pygame.Surface = Creature._backs[name]
        self.rect: pygame.Rect = self.image.get_rect(bottomleft=Monster.BOTTOM_LEFT)

    def __repr__(self):
        return f"{self.name}: {self.health}/{self.max_health}"


class Opponent(Creature):
    MID_BOTTOM = (WINDOW_WIDTH - 250, 300)

    def __init__(self, name, groups):
        super().__init__(name, groups)
        self.image: pygame.Surface = Creature._fronts[name]
        self.rect: pygame.Rect = self.image.get_rect(midbottom=Opponent.MID_BOTTOM)
