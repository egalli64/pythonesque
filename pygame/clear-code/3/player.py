"""
Master Python by making 5 games - 3: Pong

YouTube: https://www.youtube.com/watch?v=8OMghdHP-zs&t=22529s
Google Drive: https://drive.google.com/drive/folders/1cczbSYaFtVaOoigmYkd9Rj1hPbYFqC1k

My version: https://github.com/egalli64/pythonesque/ pygame/clear-code folder
"""

import pygame

from paddle import Paddle


class Player(Paddle):
    def __init__(self, viewport: pygame.Rect, groups):
        super().__init__(viewport, groups)

        self.rect.centerx = viewport.right - Paddle.BORDER_DISTANCE

    def set_direction(self, direction):
        self.direction = direction
