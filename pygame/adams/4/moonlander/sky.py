"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Moon Lander
"""
from random import randint

import pygame
import config as cfg


class Sky:
    N_STAR = 20

    def __init__(self):
        top = 0
        left = 0
        width = cfg.WINDOW.width
        height = cfg.WINDOW.height - cfg.HORIZONT
        self.rect = pygame.Rect(top, left, width, height)
        self.stars = []
        for _ in range(Sky.N_STAR):
            self.stars.append({"pos": (randint(2, self.rect.right - 1),
                                       randint(2, self.rect.right - 1)),
                               "size": randint(1, 3),
                               "duration": randint(400, 800),
                               "counter": 0,
                               "color": randint(10, 255)})

    def update(self) -> None:
        for star in self.stars:
            star["counter"] = (star["counter"] + 1) % (star["duration"] + 1)
            if star["counter"] == 0:
                star["color"] = (star["color"] + randint(0, 70)) % 256
                star["size"] = (star["size"] + 1) % 4

    def draw(self, screen) -> None:
        pygame.draw.rect(screen, "black", self.rect)
        for star in self.stars:
            pygame.draw.circle(screen, (255, 255, star["color"]), star["pos"], star["size"])
