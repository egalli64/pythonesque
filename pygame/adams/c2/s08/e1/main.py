"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Sprite collisions
"""
import pygame
from probe import Probe
from target import Target
from game import Game

TITLE = "Sprite Collisions"
WIN_SIZE = (700, 200)

# noinspection DuplicatedCode
if __name__ == "__main__":
    pygame.init()

    try:
        main_window = pygame.Window(TITLE, WIN_SIZE)
        main_surface = main_window.get_surface()

        Game.load_resources()
        Probe.load_resources()
        Target.load_resources()

        Game(main_window, main_surface).run()
    finally:
        pygame.quit()
