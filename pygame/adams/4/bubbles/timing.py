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
    """Timer in order to check time periodes."""

    def __init__(self, duration: int, with_start: bool = True) -> None:
        """Constructor

        Args:
            duration (int): duration of the time interval in milli seconds
            with_start (bool, optional): Controls if the first period will count (True) or not (False). Defaults to True.
        """
        self.duration = duration
        if with_start:
            self.next = pygame.time.get_ticks()
        else:
            self.next = pygame.time.get_ticks() + self.duration

    def is_next_stop_reached(self) -> bool:
        """Checks if the end of a time period is reached or exceeded.

        Returns:
            bool: True if the end of the period is reached or exceeded; otherwise False
        """
        if pygame.time.get_ticks() > self.next:
            self.next = pygame.time.get_ticks() + self.duration
            return True
        return False
