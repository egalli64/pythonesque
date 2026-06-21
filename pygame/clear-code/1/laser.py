"""
Master Python by making 5 games - 1: Space shooter

YouTube: https://www.youtube.com/watch?v=8OMghdHP-zs
GitHub: https://github.com/clear-code-projects/5games/tree/main/space%20shooter
Drive: https://drive.google.com/drive/folders/1bUGO9sv5SM3gYO_t9zgifedkQKHUYudO

My version: https://github.com/egalli64/pythonesque/ pygame/clear-code folder
"""

import pygame


class Laser(pygame.sprite.Sprite):
    IMAGE_FILENAME = "images/laser.png"
    SOUND_FILENAME = "audio/laser.wav"
    SPEED = 400
    _image: pygame.Surface
    _sound: pygame.mixer.Sound

    @classmethod
    def load_resources(cls):
        cls._image = pygame.image.load(Laser.IMAGE_FILENAME).convert_alpha()
        cls._sound = pygame.mixer.Sound(Laser.SOUND_FILENAME)
        cls._sound.set_volume(0.5)

    def __init__(self, mid_bottom, *groups):
        super().__init__(*groups)
        self.image = Laser._image
        self.rect: pygame.FRect = self.image.get_frect(midbottom=mid_bottom)
        Laser._sound.play()

    def update(self, dt):
        self.rect.centery -= Laser.SPEED * dt
        if self.rect.bottom < 0:
            self.kill()
