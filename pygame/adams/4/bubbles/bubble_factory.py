"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Bubble game - refactor to original BubbleContainer to BubbleFactory

Credits:
 * Fishtank image: https://www.pngwing.com/en/free-png-vadpk
 * Sound: https://www.fesliyanstudios.com/royalty-free-sound-effects-download
"""

import pygame


def clamp(value, minimum, maximum):
    return max(minimum, min(value, maximum))


class BubbleFactory:
    FILENAME = "images/bubble1.png"
    FILENAME_X = "images/bubble2.png"
    RADIUS_RANGE = (15, 240)

    @classmethod
    def load_resources(cls):
        cls._image = pygame.image.load(BubbleFactory.FILENAME).convert_alpha()
        cls._image_x = pygame.image.load(BubbleFactory.FILENAME_X).convert_alpha()

    def __init__(self):
        self.cache = {}

    def get(self, radius, plain: bool = True) -> pygame.Surface:
        radius = round(radius)
        key = (plain, radius)
        if key not in self.cache:
            image = BubbleFactory._image if plain else BubbleFactory._image_x
            size = (radius * 2, radius * 2)
            self.cache[key] = pygame.transform.scale(image, size)
        return self.cache[key]
