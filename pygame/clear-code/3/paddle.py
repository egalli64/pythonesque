"""
Master Python by making 5 games - 3: Pong

YouTube: https://www.youtube.com/watch?v=8OMghdHP-zs&t=22529s
Google Drive: https://drive.google.com/drive/folders/1cczbSYaFtVaOoigmYkd9Rj1hPbYFqC1k

My version: https://github.com/egalli64/pythonesque/ pygame/clear-code folder
"""

import pygame


class Paddle(pygame.sprite.Sprite):
    SIZE = (40, 100)
    COLORS = ("#ee322c", "#b12521")
    SPEED = 500
    BORDER_DISTANCE = 50

    def __init__(self, viewport: pygame.Rect, groups):
        super().__init__(groups)

        self.viewport: pygame.Rect = viewport
        self.image = pygame.Surface(Paddle.SIZE, pygame.SRCALPHA)
        pygame.draw.rect(self.image, Paddle.COLORS[0], self.image.get_rect(), 0, 4)
        self.shadow = self.image.copy()
        pygame.draw.rect(self.shadow, Paddle.COLORS[1], self.shadow.get_rect(), 0, 4)

        self.rect: pygame.FRect = self.image.get_frect(centery=viewport.centery)
        self.old_rect = self.rect.copy()
        self.direction = 0

    def update(self, dt):
        self.old_rect = self.rect.copy()
        self.rect.centery += self.direction * Paddle.SPEED * dt
        self.rect.clamp_ip(self.viewport)
