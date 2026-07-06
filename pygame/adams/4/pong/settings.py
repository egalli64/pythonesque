"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Pong settings
"""

import pygame


class Settings:
    """Project global settings."""

    WINDOW = pygame.Rect(0, 0, 1000, 600)
    KI = {"left": False, "right": False}
    SOUNDFLAG: bool = True
