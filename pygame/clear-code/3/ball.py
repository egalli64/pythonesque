"""
Master Python by making 5 games - 3: Pong

YouTube: https://www.youtube.com/watch?v=8OMghdHP-zs&t=22529s
Google Drive: https://drive.google.com/drive/folders/1cczbSYaFtVaOoigmYkd9Rj1hPbYFqC1k

My version: https://github.com/egalli64/pythonesque/ pygame/clear-code folder
"""

from random import choice, uniform

import pygame


class Ball(pygame.sprite.Sprite):
    SIZE = (30, 30)
    SPEED = 450
    COLOR = "#ee622c"

    def __init__(self, groups, viewport, _):
        super().__init__(groups)

        self.viewport = viewport
        self.image = pygame.Surface(Ball.SIZE, pygame.SRCALPHA)
        center = (Ball.SIZE[0] / 2, Ball.SIZE[1] / 2)
        pygame.draw.circle(self.image, Ball.COLOR, center, Ball.SIZE[0] / 2)
        self.rect: pygame.FRect = self.image.get_frect(center=viewport.center)

        x = choice((1, -1))
        y = uniform(0.7, 0.8) * choice((-1, 1))
        self.direction = pygame.Vector2(x, y)

    def move(self, dt):
        self.rect.center += self.direction * Ball.SPEED * dt

    def wall_collision(self):
        if self.rect.top <= 0:
            self.rect.top = 0
            self.direction.y *= -1

        if self.rect.bottom >= self.viewport.height:
            self.rect.bottom = self.viewport.height
            self.direction.y *= -1

        if self.rect.right >= self.viewport.width:
            self.rect.right = self.viewport.width
            self.direction.x *= -1

        if self.rect.left <= 0:
            self.rect.left = 0
            self.direction.x *= -1

    def update(self, dt):
        self.move(dt)
        self.wall_collision()
