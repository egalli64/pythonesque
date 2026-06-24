"""
Master Python by making 5 games - 2: Vampire survivor

YouTube: https://www.youtube.com/watch?v=8OMghdHP-zs&t=13523s
GitHub: https://github.com/clear-code-projects/5games/tree/main/Vampire%20survivor
Google Drive: https://drive.google.com/drive/folders/1WBhwu1yAzgmNwQ2w-SI6G8hzqwQjUN-Z

My version: https://github.com/egalli64/pythonesque/ pygame/clear-code folder
"""

from typing import override

import pygame


class CameraGroup(pygame.sprite.Group):
    def __init__(self, viewport, target):
        super().__init__()
        self.viewport = viewport
        self.target = target
        self.offset = pygame.Vector2()

    def camera_draw(self, screen):
        self.offset.x = -(self.target.rect.centerx - self.viewport.width / 2)
        self.offset.y = -(self.target.rect.centery - self.viewport.height / 2)

        layer_y = lambda sprite: (sprite.camera_layer, sprite.rect.centery)
        for sprite in sorted(self.sprites(), key=layer_y):
            screen.blit(sprite.image, sprite.rect.topleft + self.offset)
