"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Moon Lander
"""
import pygame


class Question:
    def __init__(self, viewport):
        self.font = pygame.font.Font(None, 24)
        self.surface = self.font.render("(Q)uit or (R)estart?", True, "red")
        self.rect = self.surface.get_rect()
        self.rect.centerx = viewport.centerx
        self.rect.bottom = viewport.bottom - 10

    def draw(self, screen) -> None:
        screen.blit(self.surface, self.rect.topleft)
