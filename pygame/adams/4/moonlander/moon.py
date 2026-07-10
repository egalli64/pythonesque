"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Moon Lander
"""
from random import randint

import pygame
import config as cfg


class Moon:
    LAYER_COUNT = 5
    PEAK_COUNT = 35

    def __init__(self, viewport):
        self.surface = pygame.Surface((viewport.width, cfg.HORIZONT + Moon.LAYER_COUNT * 30), pygame.SRCALPHA)
        self.rect = self.surface.get_rect()
        self.rect.left = viewport.left
        self.rect.bottom = viewport.bottom
        landingarea = pygame.Rect(0, self.rect.height - cfg.HORIZONT, viewport.width, cfg.HORIZONT)

        layers = []
        for layer_index in range(Moon.LAYER_COUNT):
            mypeaks = randint(Moon.PEAK_COUNT // 2, Moon.PEAK_COUNT)
            dist = landingarea.width // mypeaks
            mycolor = 180 - layer_index * 20
            y = landingarea.top - 10 - randint(5, 10) * layer_index
            x = landingarea.left
            lofPeaks = [(x, landingarea.top)]
            for i in range(mypeaks):
                lofPeaks.append((x, y + randint(-5, 20)))
                x += dist
            lofPeaks.append((landingarea.right, y))
            lofPeaks.append((landingarea.right, landingarea.top))

            poly = []
            for index in range(len(lofPeaks) - 1):
                p1 = lofPeaks[index]
                p2 = lofPeaks[index + 1]
                p3 = (lofPeaks[index + 1][0], landingarea.top)
                p4 = (lofPeaks[index][0], landingarea.top)
                r = randint(-5, 5)
                c = [mc + r for mc in (mycolor, mycolor, mycolor)]
                poly.append({"points": (p1, p2, p3, p4), "color": c})
            layers.append(poly)

        pygame.draw.rect(self.surface, (230, 230, 230), landingarea)
        for layer in reversed(layers):
            for poly in layer:
                pygame.draw.polygon(self.surface, poly["color"], poly["points"])

    def draw(self, screen):
        screen.blit(self.surface, self.rect.topleft)
