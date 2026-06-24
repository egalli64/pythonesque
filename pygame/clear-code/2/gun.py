"""
Master Python by making 5 games - 2: Vampire survivor

YouTube: https://www.youtube.com/watch?v=8OMghdHP-zs&t=13523s
GitHub: https://github.com/clear-code-projects/5games/tree/main/Vampire%20survivor
Google Drive: https://drive.google.com/drive/folders/1WBhwu1yAzgmNwQ2w-SI6G8hzqwQjUN-Z

My version: https://github.com/egalli64/pythonesque/ pygame/clear-code folder
"""

from math import atan2, degrees, pi

import pygame
from bullet import Bullet

WIN_RECT = pygame.Rect(0, 0, 1280, 720)


class Gun(pygame.sprite.Sprite):
    DISTANCE = 140
    FILENAME = "images/gun/gun.png"
    COOLDOWN = 0.1

    @classmethod
    def load_resources(cls):
        cls._bullet = pygame.image.load(cls.FILENAME).convert_alpha()
        cls._image = pygame.image.load(Gun.FILENAME).convert_alpha()

    def __init__(self, player, groups):
        super().__init__(groups)

        self.player = player
        self.direction = pygame.Vector2()
        self.image = Gun._image
        self.rect: pygame.FRect = self.image.get_frect(center=self.center())

        self.cooldown = 0
        self.camera_layer = 1

    def get_direction(self):
        mouse_pos = pygame.Vector2(pygame.mouse.get_pos())
        player_pos = pygame.Vector2(WIN_RECT.center)
        self.direction = (mouse_pos - player_pos).normalize()

    def rotate_gun(self):
        angle = degrees(atan2(*self.direction) - pi / 2)
        if self.direction.x > 0:
            self.image = pygame.transform.rotate(Gun._image, angle)
        else:
            self.image = pygame.transform.rotate(Gun._image, abs(angle))
            self.image = pygame.transform.flip(self.image, False, True)

    def update(self, dt):
        self.get_direction()
        self.rotate_gun()
        self.rect.center = self.center()

        self.cooldown = max(0, self.cooldown - dt)

    def center(self):
        return self.player.rect.center + self.direction * Gun.DISTANCE

    def shoot(self):
        if not self.cooldown:
            pos = self.rect.center + self.direction * 50
            self.cooldown = Gun.COOLDOWN
            return Bullet(pos, self.direction)
        else:
            return None
