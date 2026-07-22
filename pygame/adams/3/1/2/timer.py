"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Exploding rocks
"""
import pygame


class Timer:
    def __init__(self, delta: int):
        self.delta = delta
        self.next = pygame.time.get_ticks() + self.delta

    def tick(self) -> bool:
        if pygame.time.get_ticks() > self.next:
            self.next = pygame.time.get_ticks() + self.delta
            return True
        return False
