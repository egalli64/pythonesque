"""
Master Python by making 5 games - 2: Vampire survivor

YouTube: https://www.youtube.com/watch?v=8OMghdHP-zs&t=13523s
GitHub: https://github.com/clear-code-projects/5games/tree/main/Vampire%20survivor
Google Drive: https://drive.google.com/drive/folders/1WBhwu1yAzgmNwQ2w-SI6G8hzqwQjUN-Z

My version: https://github.com/egalli64/pythonesque/ pygame/clear-code folder
"""

import pygame


class Obstacle(pygame.sprite.Sprite):
    COLOR = "blue"

    def __init__(self, pos, size, groups):
        super().__init__(groups)
        self.image = pygame.Surface(size)
        self.image.fill(Obstacle.COLOR)
        self.rect = self.image.get_rect(center=pos)
