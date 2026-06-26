"""
Master Python by making 5 games - 3: Pong

YouTube: https://www.youtube.com/watch?v=8OMghdHP-zs&t=22529s
Google Drive: https://drive.google.com/drive/folders/1cczbSYaFtVaOoigmYkd9Rj1hPbYFqC1k

My version: https://github.com/egalli64/pythonesque/ pygame/clear-code folder
"""

import pygame

WIN_RECT = pygame.Rect(0, 0, 1280, 720)


class Player(pygame.sprite.Sprite):
    PADDLE_SIZE = (40, 100)
    SPEED = 500
    PADDLE_COLOR = "#ee322c"
    POS = (WIN_RECT.w - 50, WIN_RECT.h / 2)

    def __init__(self, groups):
        super().__init__(groups)

        self.image = pygame.Surface(Player.PADDLE_SIZE, pygame.SRCALPHA)
        pygame.draw.rect(self.image, Player.PADDLE_COLOR, self.image.get_rect(), 0, 4)
        self.rect: pygame.FRect = self.image.get_frect(center=Player.POS)

        self.direction = 0

    def move(self, dt):
        self.rect.centery += self.direction * Player.SPEED * dt
        self.rect.top = 0 if self.rect.top < 0 else self.rect.top
        self.rect.bottom = (
            WIN_RECT.h if self.rect.bottom > WIN_RECT.h else self.rect.bottom
        )

    def get_direction(self):
        keys = pygame.key.get_pressed()
        self.direction = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])

    def update(self, dt):
        self.get_direction()
        self.move(dt)
