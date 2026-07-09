"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Bubble game

Credits:
 * Fishtank image: https://www.pngwing.com/en/free-png-vadpk
 * Sound: https://www.fesliyanstudios.com/royalty-free-sound-effects-download
"""

import pygame


class Timer:
    def __init__(self, duration: int) -> None:
        self.duration = duration
        self.next = pygame.time.get_ticks()

    def expired(self) -> bool:
        ticks = pygame.time.get_ticks()
        if ticks > self.next:
            self.next = ticks + self.duration
            return True
        else:
            return False
