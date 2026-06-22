"""
Master Python by making 5 games - 1: Space shooter

YouTube: https://www.youtube.com/watch?v=8OMghdHP-zs
GitHub: https://github.com/clear-code-projects/5games/tree/main/space%20shooter
Drive: https://drive.google.com/drive/folders/1bUGO9sv5SM3gYO_t9zgifedkQKHUYudO

My version: https://github.com/egalli64/pythonesque/ pygame/clear-code folder
"""

import pygame
from laser import Laser

WIN_RECT = pygame.Rect(0, 0, 1280, 720)


class Player(pygame.sprite.Sprite):
    FILENAME = "images/player.png"
    _image: pygame.Surface
    SPEED = 300
    COOLDOWN = 1 / 3  # sec

    @classmethod
    def load_resources(cls):
        cls._image = pygame.image.load(Player.FILENAME).convert_alpha()

    def __init__(self, center, groups):
        super().__init__(groups)
        self.image = Player._image
        self.mask = pygame.mask.from_surface(self.image)
        self.rect: pygame.FRect = self.image.get_frect(center=center)
        self.direction = pygame.Vector2()

        self.cooldown_remaining = 0.0  # ready to shoot

    def set_direction(self, x: int, y: int):
        self.direction.update(x, y)
        if self.direction:
            self.direction.normalize_ip()

    def request_shoot(self):
        if self.cooldown_remaining == 0:
            self.cooldown_remaining = Player.COOLDOWN
            return Laser(self.rect.midtop)
        else:
            return None

    def update(self, dt):
        self.rect.center += self.direction * Player.SPEED * dt
        self.cooldown_remaining = max(0, self.cooldown_remaining - dt)
