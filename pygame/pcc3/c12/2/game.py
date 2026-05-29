"""
Python Crash Course, Third Edition, Part II https://nostarch.com/python-crash-course-3rd-edition
My notes: https://github.com/egalli64/pythonesque/pygame/pcc3

Chapter 12 - A Ship that fires bullets
Piloting the Ship
"""

import pygame

from ship import Ship

FPS = 30

GAME_NAME = "Alien Invasion"

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
BACKGROUND_COLOR = (230, 230, 230)  # light gray


class Game:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption(GAME_NAME)

        self.ship = Ship(self.screen)

    def _check_keydown_events(self, event):
        """
        Respond to keydown events

        return False on terminating events
        """
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            return False

        return True

    def _check_keyup_events(self, event):
        """
        Respond to keyup events

        return False on terminating events
        """
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

        return True

    def _check_events(self):
        """
        Watch for keyboard and mouse events

        return False on terminating events
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                return self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                return self._check_keyup_events(event)

        return True

    def _update_screen(self):
        """Redraw the screen during each pass through the loop"""
        self.screen.fill(BACKGROUND_COLOR)
        self.ship.blit()

        # Make the most recently drawn screen visible.
        pygame.display.flip()

    def run(self):
        """The game main loop"""
        while self._check_events():
            self.ship.update()

            self._update_screen()
            self.clock.tick(FPS)


if __name__ == "__main__":
    # Make a game instance, and run the game.
    ai = Game()
    ai.run()

    print("Done.")
