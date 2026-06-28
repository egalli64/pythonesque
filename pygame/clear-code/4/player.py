"""
Master Python by making 5 games - 4: Platformer

YouTube: https://www.youtube.com/watch?v=8OMghdHP-zs&t=26735s
GitHub: https://github.com/clear-code-projects/5games/tree/main/Platform
Google Drive: https://drive.google.com/drive/folders/1FCSPHzD9R4RBUypDTB_FIfwlyiCLA5WN

My version: https://github.com/egalli64/pythonesque/ pygame/clear-code folder
"""

import pygame
from sprite import Sprite


class Player(Sprite):
    SPEED = 500

    def __init__(self, pos, groups, collision_sprites):
        image = pygame.Surface((40, 80))
        super().__init__(pos, image, groups)

        self.direction = pygame.Vector2()
        self.collision_sprites = collision_sprites

    def set_direction(self, x: int, y: int):
        self.direction.update(x, y)
        if self.direction:
            self.direction.normalize_ip()

    def horizontal_collision(self):
        for sprite in self.collision_sprites:
            if sprite.rect.colliderect(self.rect):
                if self.direction.x > 0:
                    self.rect.right = sprite.rect.left
                if self.direction.x < 0:
                    self.rect.left = sprite.rect.right

    def vertical_collision(self):
        for sprite in self.collision_sprites:
            if sprite.rect.colliderect(self.rect):
                if self.direction.y > 0:
                    self.rect.bottom = sprite.rect.top
                if self.direction.y < 0:
                    self.rect.top = sprite.rect.bottom

    def update(self, dt):
        self.rect.x += self.direction.x * Player.SPEED * dt
        self.horizontal_collision()
        self.rect.y += self.direction.y * Player.SPEED * dt
        self.vertical_collision()
