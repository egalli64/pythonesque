"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

A running cat
"""
import pygame


class Timer:
    MIN_DURATION = 10

    def __init__(self, duration: int):
        self.duration = duration
        self.next = pygame.time.get_ticks() + duration

    def tick(self) -> bool:
        if pygame.time.get_ticks() > self.next:
            self.next = pygame.time.get_ticks() + self.duration
            return True
        return False

    def change_duration(self, delta: int):
        self.duration = max(Timer.MIN_DURATION, self.duration + delta)
