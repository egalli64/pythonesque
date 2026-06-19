"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Pong events
"""

from random import choice, randint
import pygame


class Events:
    POINT_FOR = pygame.event.custom_type()
    MYEVENT = pygame.event.Event(POINT_FOR, player=0)
