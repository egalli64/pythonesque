"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Stereo sound
"""
import pygame


class Ground:
    FILENAME = "../images/background.png"
    TILE_SIZE = (32, 32)  # square tile, in bit

    @classmethod
    def load_resources(cls) -> None:
        cls._tile = pygame.image.load(Ground.FILENAME).convert()
        if cls._tile.get_size() != Ground.TILE_SIZE:
            print("Warning: unexpected tile size!")
            cls._tile = pygame.transform.scale(cls._tile, Ground.TILE_SIZE)

    def __init__(self, viewport: pygame.Rect) -> None:
        self.background = pygame.Surface(viewport.size)

        for x in range(0, viewport.width, Ground._tile.get_width()):
            for y in range(0, viewport.height, Ground._tile.get_height()):
                self.background.blit(Ground._tile, (x, y))

    def draw(self, screen):
        screen.blit(self.background, (0, 0))
