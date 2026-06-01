"""
Python Crash Course, Third Edition, Part II https://nostarch.com/python-crash-course-3rd-edition
My notes: https://github.com/egalli64/pythonesque/ pygame/pcc3 folder

Chapter 14 - Scoring
Scoring
"""

import pygame.font
from pygame.sprite import Group

from ship import Ship


class Scoreboard:
    """A class to report scoring information."""

    TEXT_COLOR = (30, 30, 30)
    BACKGROUND_COLOR = (230, 230, 230)  # light gray
    FONT_SIZE = 48

    ALIEN_POINTS = 50

    def __init__(self, screen):
        """Initialize scorekeeping attributes."""
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        self.font = pygame.font.SysFont(None, Scoreboard.FONT_SIZE)

        self.score = 0

        self.prep_score()

    def prep_score(self):
        """Turn the score into a rendered image."""
        self.score_image = self.font.render(
            str(self.score), True, Scoreboard.TEXT_COLOR, Scoreboard.BACKGROUND_COLOR
        )
        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def draw(self):
        """Draw scores, level, and ships to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
