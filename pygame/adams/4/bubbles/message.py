"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Bubble game

Credits:
 * Fish tank image: https://www.pngwing.com/en/free-png-vadpk
 * Sound: https://www.fesliyanstudios.com/royalty-free-sound-effects-download
"""
from enum import Enum

import pygame


class Message:
    image: pygame.Surface
    rect: pygame.Rect

    PAUSE_FILENAME = "images/pause.png"
    RESTART_FILENAME = "images/restart.png"

    class Type(Enum):
        PAUSE = 0
        RESTART = 1
        NONE = 2

    @classmethod
    def load_resources(cls):
        pause = pygame.image.load(Message.PAUSE_FILENAME).convert_alpha()
        restart = pygame.image.load(Message.RESTART_FILENAME).convert_alpha()
        cls._images = (pause, restart)
        cls._rects = (pause.get_rect(), restart.get_rect())

    def __init__(self):
        self.status = Message.Type.NONE

    def set_status(self, status: Message.Type = Type.NONE):
        self.status = status
        if status != Message.Type.NONE:
            self.image = Message._images[self.status.value]
            self.rect = Message._rects[self.status.value]

    def draw(self, screen):
        if self.status != Message.Type.NONE:
            screen.blit(self.image, self.rect)
