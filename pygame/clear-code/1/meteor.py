"""
Master Python by making 5 games - 1: Space shooter

YouTube: https://www.youtube.com/watch?v=8OMghdHP-zs
GitHub: https://github.com/clear-code-projects/5games/tree/main/space%20shooter
Drive: https://drive.google.com/drive/folders/1bUGO9sv5SM3gYO_t9zgifedkQKHUYudO

My version: https://github.com/egalli64/pythonesque/ pygame/clear-code folder
"""

from random import randint, uniform
import pygame


class Meteor(pygame.sprite.Sprite):
    FILENAME = "images/meteor.png"
    _image: pygame.Surface

    @classmethod
    def load_resources(cls):
        cls._image = pygame.image.load(Meteor.FILENAME).convert_alpha()

    def __init__(self, x_pos, groups):
        super().__init__(groups)
        self.image = Meteor._image
        self.rect: pygame.FRect = self.image.get_frect(center=(x_pos, 0))
        self.start_time = pygame.time.get_ticks()
        self.lifetime = 3000
        self.direction = pygame.Vector2(uniform(-0.5, 0.5), 1)
        self.speed = randint(400, 500)
        self.rotation_speed = randint(40, 80)
        self.rotation = 0

    def update(self, dt):
        self.rect.center += self.direction * self.speed * dt
        if pygame.time.get_ticks() - self.start_time >= self.lifetime:
            self.kill()
        self.rotation += self.rotation_speed * dt
        self.image = pygame.transform.rotate(Meteor._image, self.rotation)
        self.rect = self.image.get_frect(center=self.rect.center)
