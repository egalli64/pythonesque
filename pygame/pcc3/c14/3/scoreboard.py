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

    BASE_ALIEN_POINTS = 50
    SCORE_SCALE = 1.5

    def __init__(self, screen):
        """Initialize scorekeeping attributes."""
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        self.font = pygame.font.SysFont(None, Scoreboard.FONT_SIZE)

        self.high_score = 0
        self.init_score()

        self.prep_score()
        self.prep_high_score()

    def increase_alien_points(self):
        self.alien_points = int(self.alien_points * Scoreboard.SCORE_SCALE)

    def alien_hit(self, n):
        """Adjust the score for n alien hits"""
        self.score += self.alien_points * n
        self.prep_score()
        self.check_high_score()

    def init_score(self):
        self.score = 0
        self.alien_points = Scoreboard.BASE_ALIEN_POINTS
        self.prep_score()

    def check_high_score(self):
        """Check to see if there's a new high score."""
        if self.score > self.high_score:
            self.high_score = self.score
            self.prep_high_score()

    def prep_score(self):
        """Turn the score into a rendered image."""
        rounded = f"{(round(self.score, -1)):,}"
        self.score_image = self.font.render(
            rounded, True, Scoreboard.TEXT_COLOR, Scoreboard.BACKGROUND_COLOR
        )
        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """Turn the high score into a rendered image."""
        rounded = f"{round(self.high_score, -1):,}"
        self.high_score_image = self.font.render(
            rounded, True, Scoreboard.TEXT_COLOR, Scoreboard.BACKGROUND_COLOR
        )
        # Center the high score at the top of the screen.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def draw(self):
        """Draw info from the scoreboard"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
