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


class Gun(pygame.sprite.Sprite):
    DISTANCE = 140
    PLAYER_CENTER_DISPLACEMENT = 60
    BULLET_START = 50
    IMAGE_FILENAME = "images/gun/gun.png"
    SOUND_FILENAME = "audio/shoot.wav"
    COOLDOWN = 0.1

    @classmethod
    def load_resources(cls):
        cls._image = pygame.image.load(Gun.IMAGE_FILENAME).convert_alpha()
        cls._shot = pygame.mixer.Sound(cls.SOUND_FILENAME)
        cls._shot.set_volume(0.2)

    def __init__(self, player, pos):
        super().__init__()

        self.player = player
        self.shooting_focus = pos[0], pos[1] - Gun.PLAYER_CENTER_DISPLACEMENT
        self.direction = pygame.Vector2()
        self.image = Gun._image
        self.rect: pygame.FRect = self.image.get_frect(center=self.center())

        self.cooldown = 0
        self.camera_layer = 2

    def get_direction(self):
        mouse_pos = pygame.Vector2(pygame.mouse.get_pos())
        if mouse_pos != self.shooting_focus:
            self.direction = (mouse_pos - self.shooting_focus).normalize()

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
            pos = self.rect.center + self.direction * Gun.BULLET_START
            self.cooldown = Gun.COOLDOWN
            Gun._shot.play()
            return Bullet(pos, self.direction)
        else:
            return None
