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
    SPEED_RANGE = (400, 500)
    ROTATION_SPEED_RANGE = (40, 80)
    MAX_LIFETIME = 3.0  # sec
    _image: pygame.Surface

    @classmethod
    def load_resources(cls):
        cls._image = pygame.image.load(Meteor.FILENAME).convert_alpha()

    def __init__(self, x_pos, groups):
        super().__init__(groups)
        self.image = Meteor._image
        self.mask = pygame.mask.from_surface(self.image)
        self.rect: pygame.FRect = self.image.get_frect(center=(x_pos, 0))
        self.lifetime = Meteor.MAX_LIFETIME
        self.direction = pygame.Vector2(uniform(-0.5, 0.5), 1)
        self.speed = randint(*Meteor.SPEED_RANGE)
        self.rotation_speed = randint(*Meteor.ROTATION_SPEED_RANGE)
        self.rotation = 0

    def update(self, dt):
        self.rect.center += self.direction * self.speed * dt
        self.lifetime = max(0, self.lifetime - dt)

        if self.lifetime == 0:
            self.kill()
        else:
            self.rotation += self.rotation_speed * dt
            self.image = pygame.transform.rotate(Meteor._image, self.rotation)
            self.mask = pygame.mask.from_surface(self.image)
            self.rect = self.image.get_frect(center=self.rect.center)
