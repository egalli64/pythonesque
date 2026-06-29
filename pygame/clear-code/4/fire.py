"""
Master Python by making 5 games - 4: Platformer

YouTube: https://www.youtube.com/watch?v=8OMghdHP-zs&t=26735s
GitHub: https://github.com/clear-code-projects/5games/tree/main/Platform
Google Drive: https://drive.google.com/drive/folders/1FCSPHzD9R4RBUypDTB_FIfwlyiCLA5WN

My version: https://github.com/egalli64/pythonesque/ pygame/clear-code folder
"""

import pygame
from sprite import Sprite
from timer import Timer # type: ignore


class Fire(Sprite):
    FILENAME = "images/gun/fire.png"

    @classmethod
    def load_resources(cls):
        cls._image = pygame.image.load(cls.FILENAME).convert_alpha()

    def __init__(self, pos, groups, player):
        super().__init__(pos, Fire._image, groups)
        self.player = player
        self.flip = player.flip
        self.timer = Timer(100, autostart=True, func=self.kill)
        self.y_offset = pygame.Vector2(0, 8)
        if self.player.flip:
            self.rect.midright = self.player.rect.midleft + self.y_offset
            self.image = pygame.transform.flip(self.image, True, False)
        else:
            self.rect.midleft = self.player.rect.midright + self.y_offset

    def update(self, _):
        self.timer.update()

        if self.player.flip:
            self.rect.midright = self.player.rect.midleft + self.y_offset
        else:
            self.rect.midleft = self.player.rect.midright + self.y_offset

        if self.flip != self.player.flip:
            self.kill()
