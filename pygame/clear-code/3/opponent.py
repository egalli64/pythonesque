"""
Master Python by making 5 games - 3: Pong

YouTube: https://www.youtube.com/watch?v=8OMghdHP-zs&t=22529s
Google Drive: https://drive.google.com/drive/folders/1cczbSYaFtVaOoigmYkd9Rj1hPbYFqC1k

My version: https://github.com/egalli64/pythonesque/ pygame/clear-code folder
"""

import pygame

from paddle import Paddle
from ball import Ball


class Opponent(Paddle):
    TOLERANCE = 10

    def __init__(self, ball, viewport: pygame.Rect, groups):
        super().__init__(viewport, groups)
        self.ball: Ball = ball
        self.rect.centerx = Paddle.BORDER_DISTANCE

    def set_direction(self):
        target = self.ball.rect if self.ball.direction.x < 0 else self.viewport

        if self.rect.centery > target.centery + Opponent.TOLERANCE:
            self.direction = -1
        elif self.rect.centery < target.centery - Opponent.TOLERANCE:
            self.direction = 1
        else:
            self.direction = 0

    def update(self, dt):
        self.set_direction()
        super().update(dt)
