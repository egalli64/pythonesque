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
    PADDING = (20, 20)
    VERTICAL_ADJUSTMENT = 2

    @classmethod
    def load_resources(cls):
        cls._font = pygame.font.Font(None, cls.FONT_SIZE)

    def __init__(self, x, y):
        self.midbottom = x, y

    def update(self):
        score = pygame.time.get_ticks() // 100
        text_surface = Score._font.render(str(score), True, Score.COLOR)
        box_rect = text_surface.get_rect().inflate(*Score.PADDING)

        self.image = pygame.Surface(box_rect.size, pygame.SRCALPHA)
        pygame.draw.rect(self.image, Score.COLOR, self.image.get_rect(), 4, 10)
        text_pos = text_surface.get_rect(center=self.image.get_rect().center)
        text_pos.bottom += Score.VERTICAL_ADJUSTMENT
        self.image.blit(text_surface, text_pos)
        self.rect = self.image.get_rect(midbottom=self.midbottom)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
