"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Stereo sound
"""
import pygame

TILE_SIZE = 32  # square tile, in bit


class Ground:
    IMAGE = "../images/background.png"

    def __init__(self, viewport: pygame.Rect) -> None:
        tile = pygame.image.load(Ground.IMAGE).convert()
        assert tile.get_width() == tile.get_height() == TILE_SIZE, "Bad tile size"

        self.background = pygame.Surface(viewport.size)

        for x in range(0, viewport.width, tile.get_width()):
            for y in range(0, viewport.height, tile.get_height()):
                self.background.blit(tile, (x, y))

    def draw(self, screen):
        screen.blit(self.background, (0, 0))
