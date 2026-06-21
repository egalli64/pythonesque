"""
Master Python by making 5 games - 1: Space shooter

YouTube: https://www.youtube.com/watch?v=8OMghdHP-zs
GitHub: https://github.com/clear-code-projects/5games/tree/main/space%20shooter
Drive: https://drive.google.com/drive/folders/1bUGO9sv5SM3gYO_t9zgifedkQKHUYudO

My version: https://github.com/egalli64/pythonesque/ pygame/clear-code folder
"""

import pygame


class Explosion(pygame.sprite.Sprite):
    FRAME_TEMPLATE = "images/explosion/{:d}.png"
    FRAME_COUNT = 21
    SOUND_FILENAME = "audio/explosion.wav"
    DURATION_MODIFIER = 20  # decrease it for longer lasting explosion

    @classmethod
    def load_resources(cls):
        cls._frames = [
            pygame.image.load(cls.FRAME_TEMPLATE.format(i)).convert_alpha()
            for i in range(cls.FRAME_COUNT)
        ]
        cls._sound = pygame.mixer.Sound(cls.SOUND_FILENAME)

    def __init__(self, pos, groups):
        super().__init__(groups)
        self.fractional_index = 0.0
        self.image = Explosion._frames[0]
        self.rect = self.image.get_rect(center=pos)
        Explosion._sound.play()

    def update(self, dt):
        self.fractional_index += dt * Explosion.DURATION_MODIFIER
        if self.fractional_index >= len(self._frames):
            self.kill()
        else:
            self.image = Explosion._frames[int(self.fractional_index)]
