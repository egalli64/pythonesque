"""
Master Python by making 5 games - 5: Monster battle

YouTube: https://www.youtube.com/watch?v=8OMghdHP-zs&t=32960s
GitHub: https://github.com/clear-code-projects/5games/tree/main/Monster%20battle
Google Drive: https://drive.google.com/drive/folders/15VQ37pgCwXxHZ8oBK0yc_CzKQeP2qSSl

My version: https://github.com/egalli64/pythonesque/ pygame/clear-code folder
"""

import pygame
from support import import_tiles, audio_importer


class Attack(pygame.sprite.Sprite):
    PATH_FRAMES = "images/attacks"
    N_SLICES = 4
    PATH_AUDIO = "audio/attacks"

    @classmethod
    def load_resources(cls):
        cls._frames = import_tiles(cls.N_SLICES, cls.PATH_FRAMES)
        cls.audio = audio_importer(cls.PATH_AUDIO)

    def __init__(self, kind, target, groups):
        super().__init__(groups)
        self.frames = Attack._frames[kind]
        self.frame_index = 0
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_frect(center=target.rect.center)
        self.audio[kind].play()

    def update(self, dt):
        self.frame_index += 5 * dt
        if self.frame_index < len(self.frames):
            self.image = self.frames[int(self.frame_index)]
        else:
            self.kill()
