"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

A running cat - dt from main loop
"""
import pygame


class Animation:
    MIN_DURATION = 0.01
    DEFAULT_DURATION_TIME = 0.1

    def __init__(self, filenames, colorkey, duration=DEFAULT_DURATION_TIME):
        self.frames: list[pygame.Surface] = []
        for filename in filenames:
            bitmap = pygame.image.load(filename).convert()
            bitmap.set_colorkey(colorkey)
            self.frames.append(bitmap)

        self.duration = duration
        self.timer = 0.0
        self.index = 0

    def update(self, dt):
        self.timer += dt

        while self.timer >= self.duration:
            self.timer -= self.duration
            self.index = (self.index + 1) % len(self.frames)

    def change_duration(self, increase: bool):
        delta = Animation.MIN_DURATION * (1 if increase else -1)
        self.duration = max(Animation.MIN_DURATION, self.duration + delta)

    @property
    def image(self):
        return self.frames[self.index]
