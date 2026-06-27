"""
Master Python by making 5 games - 3: Pong

YouTube: https://www.youtube.com/watch?v=8OMghdHP-zs&t=22529s
Google Drive: https://drive.google.com/drive/folders/1cczbSYaFtVaOoigmYkd9Rj1hPbYFqC1k

My version: https://github.com/egalli64/pythonesque/ pygame/clear-code folder
"""

import pygame


class Shadowed(pygame.sprite.Group):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen

    def draw(self):  # type: ignore
        for sprite in self:
            for i in range(5):
                pos = sprite.rect.left + i, sprite.rect.top + i
                self.screen.blit(sprite.shadow, pos)

        for sprite in self:
            self.screen.blit(sprite.image, sprite.rect)
