"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Collision between a sprite and a group of sprites
"""
import pygame


class Block(pygame.sprite.Sprite):
    COLOR = (200, 50, 50)
    SIZE = (30, 30)

    image: pygame.Surface
    rect: pygame.Rect

    def __init__(self, pos: tuple[int, int]) -> None:
        super().__init__()

        self.image = pygame.Surface(Block.SIZE)
        self.image.fill(Block.COLOR)
        self.rect = self.image.get_rect(center=pos)
