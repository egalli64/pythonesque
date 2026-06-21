"""
Master Python by making 5 games - 1: Space shooter

YouTube: https://www.youtube.com/watch?v=8OMghdHP-zs
GitHub: https://github.com/clear-code-projects/5games/tree/main/space%20shooter
Drive: https://drive.google.com/drive/folders/1bUGO9sv5SM3gYO_t9zgifedkQKHUYudO

My version: https://github.com/egalli64/pythonesque/ pygame/clear-code folder
"""

import pygame


class Score:
    FONT_SIZE = 40
    COLOR = "gray94"

    @classmethod
    def load_resources(cls):
        cls._font = pygame.font.Font(None, cls.FONT_SIZE)

    def __init__(self, pos):
        self.pos = pos[0], pos[1] - 50

    def update(self):
        score = pygame.time.get_ticks() // 100
        self.image = Score._font.render(str(score), True, Score.COLOR)
        self.rect = self.image.get_rect(midbottom=self.pos)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        rect = self.rect.inflate(20, 10).move(0, -2)
        pygame.draw.rect(screen, Score.COLOR, rect, 4, 10)
