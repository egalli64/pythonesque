"""
Master Python by making 5 games - 2: Vampire survivor

YouTube: https://www.youtube.com/watch?v=8OMghdHP-zs&t=13523s
GitHub: https://github.com/clear-code-projects/5games/tree/main/Vampire%20survivor
Google Drive: https://drive.google.com/drive/folders/1WBhwu1yAzgmNwQ2w-SI6G8hzqwQjUN-Z

My version: https://github.com/egalli64/pythonesque/ pygame/clear-code folder
"""

import pygame


class Bullet(pygame.sprite.Sprite):
    FILENAME = "images/gun/bullet.png"
    LIFETIME = 1000
    SPEED = 1200

    @classmethod
    def load_resources(cls):
        cls._image = pygame.image.load(cls.FILENAME).convert_alpha()

    def __init__(self, pos, direction, groups):
        super().__init__(groups)
        self.image = Bullet._image
        self.rect: pygame.FRect = Bullet._image.get_frect(center=pos)
        self.spawn_time = pygame.time.get_ticks()

        self.direction = direction
        self.camera_layer = 1

    def update(self, dt):
        self.rect.center += self.direction * Bullet.SPEED * dt

        if pygame.time.get_ticks() - self.spawn_time >= Bullet.LIFETIME:
            self.kill()
