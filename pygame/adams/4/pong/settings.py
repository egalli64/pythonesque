"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Pong settings
"""

import os
import pygame


class Settings:
    """Project global settings."""

    WINDOW = pygame.Rect(0, 0, 1000, 600)
    FPS = 60
    KI = {"left": False, "right": False}
    SOUNDFLAG: bool = True
    PATH = {}
    PATH["file"] = os.path.dirname(os.path.abspath(__file__))
    PATH["sound"] = os.path.join(PATH["file"], "sounds")

    @staticmethod
    def get_sound(filename: str) -> str:
        return os.path.join(Settings.PATH["sound"], filename)
