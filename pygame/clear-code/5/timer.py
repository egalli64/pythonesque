"""
Master Python by making 5 games - 5: Monster battle

YouTube: https://www.youtube.com/watch?v=8OMghdHP-zs&t=32960s
GitHub: https://github.com/clear-code-projects/5games/tree/main/Monster%20battle
Google Drive: https://drive.google.com/drive/folders/15VQ37pgCwXxHZ8oBK0yc_CzKQeP2qSSl

My version: https://github.com/egalli64/pythonesque/ pygame/clear-code folder
"""

import pygame


class Timer:
    def __init__(self, duration, repeat=False, autostart=False, func=None):
        self.duration = duration
        self.activation_time = 0
        self.repeat = repeat
        self.func = func

        if autostart:
            self.activate()

    def __bool__(self):
        return self.activation_time != 0

    def activate(self):
        self.activation_time = pygame.time.get_ticks()

    def deactivate(self):
        self.activation_time = pygame.time.get_ticks() if self.repeat else 0

    def update(self):
        if pygame.time.get_ticks() - self.activation_time >= self.duration:
            if self.func and self.activation_time != 0:
                self.func()
            self.deactivate()
