"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Pong help
"""
from typing import Tuple
import pygame
from settings import Settings


class Help(pygame.sprite.Sprite):
    def __init__(self, *groups: Tuple[pygame.sprite.Group]) -> None:
        super().__init__(*groups)
        self.rect = pygame.Rect(Settings.WINDOW.topleft, Settings.WINDOW.size)
        self.image = pygame.Surface(self.rect.size).convert_alpha()
        self.image.fill([20, 20, 20, 200])
        font = pygame.font.Font(pygame.font.get_default_font(), 20)
        text_l = "h\np\nESC\n\nF2\nk\nl\nr\n\nUP\nDOWN\nw\ns"
        text_r = (
            "- toggle help mode\n- toggle pause mode\n- quit\n\n- toggle sound mode\n"
        )
        text_r += "- toggle both paddles AI mode\n- toggle left paddle AI mode\n- toggle right paddle AI mode\n\n"
        text_r += "- move left paddle up\n- move left paddle down\n- move right paddle up\n- move right paddle down"
        lines = font.render(text_l, True, "white")
        self.image.blit(lines, (10, 10))
        lines = font.render(text_r, True, "white")
        self.image.blit(lines, (10 + 70, 10))
