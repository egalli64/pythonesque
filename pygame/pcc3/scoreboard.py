"""
Python Crash Course, Third Edition, Part II https://nostarch.com/python-crash-course-3rd-edition
My version: https://github.com/egalli64/pythonesque/ pygame/pcc3 folder
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

    SHIP_COUNT = 3

    def __init__(self, screen):
        """Initialize scorekeeping attributes."""
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        self.font = pygame.font.SysFont(None, Scoreboard.FONT_SIZE)

        self.set_current_info()
        self.set_high_score(0)
        self.prep_ships()

    def increase_level(self):
        self.alien_points = int(self.alien_points * Scoreboard.SCORE_SCALE)
        self.level += 1
        self.prep_level()

    def alien_hit(self, n):
        """Adjust the score for n alien hits"""
        self.score += self.alien_points * n
        self.prep_score()
        if self.score > self.high_score:
            self.set_high_score(self.score)

    def ship_hit(self):
        self.ships_left -= 1
        self.prep_ships()

        return self.ships_left > 0

    def set_current_info(self):
        self.level = 1
        self.score = 0
        self.alien_points = Scoreboard.BASE_ALIEN_POINTS
        self.ships_left = Scoreboard.SHIP_COUNT

        self.prep_score()
        self.prep_level()

    def prep_ships(self):
        """Show how many ships are left."""
        self.ships = Group()
        for i in range(self.ships_left):
            ship = Ship(self.screen)
            ship.rect.x = 10 + i * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def prep_level(self):
        """Turn the level into a rendered image."""
        self.level_image = self.font.render(
            str(self.level), True, Scoreboard.TEXT_COLOR, Scoreboard.BACKGROUND_COLOR
        )
        # Position the level below the score.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

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

    def set_high_score(self, x):
        """Set high score as int and image (rounded to 10)"""
        self.high_score = x
        rounded = f"{round(x, -1):,}"
        self.high_score_image = self.font.render(
            rounded, True, Scoreboard.TEXT_COLOR, Scoreboard.BACKGROUND_COLOR
        )
        # Center the high score at the top of the screen.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def draw(self):
        """Draw info from the scoreboard"""
        self.screen.blit(self.level_image, self.level_rect)
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.ships.draw(self.screen)
