"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Moon Lander
"""
from random import randint

import pygame


class Moon:
    LAYER_COUNT = 5
    PEAK_COUNT = 35

    def __init__(self, viewport, horizont):
        surface_size = (viewport.width, horizont + Moon.LAYER_COUNT * 30)
        self.surface = pygame.Surface(surface_size, pygame.SRCALPHA)
        self.rect = self.surface.get_rect()
        self.rect.left = viewport.left
        self.rect.bottom = viewport.bottom
        landing_area = pygame.Rect(0, self.rect.height - horizont, viewport.width, horizont)

        layers = []
        for layer_index in range(Moon.LAYER_COUNT):
            mypeaks = randint(Moon.PEAK_COUNT // 2, Moon.PEAK_COUNT)
            dist = landing_area.width // mypeaks
            mycolor = 180 - layer_index * 20
            y = landing_area.top - 10 - randint(5, 10) * layer_index
            x = landing_area.left
            peaks = [(x, landing_area.top)]
            for i in range(mypeaks):
                peaks.append((x, y + randint(-5, 20)))
                x += dist
            peaks.append((landing_area.right, y))
            peaks.append((landing_area.right, landing_area.top))

            poly = []
            for index in range(len(peaks) - 1):
                p1 = peaks[index]
                p2 = peaks[index + 1]
                p3 = (peaks[index + 1][0], landing_area.top)
                p4 = (peaks[index][0], landing_area.top)
                r = randint(-5, 5)
                c = [mc + r for mc in (mycolor, mycolor, mycolor)]
                poly.append({"points": (p1, p2, p3, p4), "color": c})
            layers.append(poly)

        pygame.draw.rect(self.surface, (230, 230, 230), landing_area)
        for layer in reversed(layers):
            for poly in layer:
                pygame.draw.polygon(self.surface, poly["color"], poly["points"])

    def draw(self, screen):
        screen.blit(self.surface, self.rect.topleft)
