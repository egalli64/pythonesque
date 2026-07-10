"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Moon Lander
"""
from random import randint

import pygame
import config as cfg


class Moon:
    def __init__(self, screen: pygame.Surface, layer_count: int = 5, peaks: int = 35):
        self.screen = screen
        self.surface = pygame.Surface((cfg.WINDOW.width,
                                       cfg.HORIZONT + layer_count * 30),
                                      pygame.SRCALPHA)
        self.rect = self.surface.get_rect()
        self.rect.left = cfg.WINDOW.left
        self.rect.bottom = cfg.WINDOW.bottom
        landingarea = pygame.Rect(0, self.rect.height - cfg.HORIZONT,
                                  cfg.WINDOW.width, cfg.HORIZONT)

        layers = []
        for layer_index in range(layer_count):
            mypeaks = randint(peaks // 2, peaks)
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
                pygame.draw.polygon(
                    self.surface,
                    poly["color"],
                    poly["points"])

    def draw(self):
        self.screen.blit(self.surface, self.rect.topleft)
