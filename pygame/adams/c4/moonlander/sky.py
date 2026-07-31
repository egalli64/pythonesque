"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Moon Lander
"""
from random import randint

import pygame


class Sky:
    N_STAR = 20

    def __init__(self, rect: pygame.Rect) -> None:
        self.rect = rect
        self.stars = []
        for _ in range(Sky.N_STAR):
            self.stars.append(Star(rect))

    def update(self) -> None:
        for star in self.stars:
            star.update()

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.rect(screen, "black", self.rect)
        for star in self.stars:
            star.draw(screen)


class Star:
    BOTTOM_DELTA = 50
    BORDER_DELTA = 2
    SIZE_INTERVAL = (1, 4)
    DURATION_INTERVAL = (400, 600)
    BLUE_INTERVAL = (10, 255)
    BLUE_DELTA = 10

    def __init__(self, rect: pygame.Rect) -> None:
        x = randint(Star.BORDER_DELTA, rect.right - Star.BORDER_DELTA)
        y = randint(Star.BORDER_DELTA, rect.bottom - Star.BOTTOM_DELTA)
        self.pos = (x, y)
        self.size = randint(*Star.SIZE_INTERVAL)
        self.color = (255, 255, randint(*Star.BLUE_INTERVAL))
        self.duration = randint(*Star.DURATION_INTERVAL)
        self.counter = 0

    def update(self) -> None:
        self.counter = (self.counter + 1) % self.duration
        if self.counter == 0:
            self.size = randint(*Star.SIZE_INTERVAL)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, self.color, self.pos, self.size)
