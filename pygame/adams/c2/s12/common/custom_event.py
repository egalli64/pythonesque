"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

User defined events
"""
from enum import IntEnum
import pygame


class CustomEvent(IntEnum):
    OVERFLOW = pygame.event.custom_type()
    BUTTON_PRESSED = pygame.event.custom_type()
    NEW_PARTICLE = pygame.event.custom_type()
