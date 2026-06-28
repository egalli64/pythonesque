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
    GRAVITY = 50
    JUMP_SPEED = -20

    def __init__(self, pos, groups, obstacles):
        image = pygame.Surface((40, 80))
        super().__init__(pos, image, groups)

        self.direction = pygame.Vector2()
        self.obstacles = obstacles
        self.on_floor = False

    def set_horizontal_direction(self, x: int):
        self.direction.x = x

    def jump(self):
        if self.on_floor:
            self.direction.y = Player.JUMP_SPEED

    def horizontal_collision(self):
        for obstacle in self.obstacles:
            if obstacle.rect.colliderect(self.rect):
                if self.direction.x > 0:
                    self.rect.right = obstacle.rect.left
                if self.direction.x < 0:
                    self.rect.left = obstacle.rect.right

    def vertical_collision(self):
        for obstacle in self.obstacles:
            if obstacle.rect.colliderect(self.rect):
                if self.direction.y > 0:
                    self.rect.bottom = obstacle.rect.top
                if self.direction.y < 0:
                    self.rect.top = obstacle.rect.bottom
                self.direction.y = 0

    def check_floor(self):
        probe = self.rect.inflate(-10, 0)
        probe.height = 2
        probe.top = self.rect.bottom

        self.on_floor = any(probe.colliderect(x.rect) for x in self.obstacles)

    def update(self, dt):
        self.check_floor()
        self.rect.x += self.direction.x * Player.SPEED * dt
        self.horizontal_collision()

        self.direction.y += Player.GRAVITY * dt
        self.rect.y += self.direction.y
        self.vertical_collision()
