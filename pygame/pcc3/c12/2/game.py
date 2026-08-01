"""
Python Crash Course, Third Edition, Part II https://nostarch.com/python-crash-course-3rd-edition
My notes: https://github.com/egalli64/pythonesque/ pygame/pcc3 folder

Chapter 12 - A Ship that fires bullets
Piloting the Ship
"""
import pygame

from ship import Ship

GAME_NAME = "Alien Invasion"
FPS = 30

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
BACKGROUND_COLOR = (230, 230, 230)  # light gray


class Game:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption(GAME_NAME)

        self.ship = Ship(self.screen)
        self.running = True

    def _check_keydown_events(self, event) -> None:
        """
        Respond to keydown events
        """
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            self.running = False

    def _check_keyup_events(self, event) -> None:
        """
        Respond to keyup events
        """
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def check_events(self) -> None:
        """
        Watch for keyboard and mouse events
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _update_screen(self):
        """Redraw the screen during each pass through the loop"""
        self.screen.fill(BACKGROUND_COLOR)
        self.ship.blit()

        # Make the most recently drawn screen visible.
        pygame.display.flip()

    def run(self):
        """The game main loop"""
        clock = pygame.time.Clock()

        while self.running:
            clock.tick(FPS)

            self.check_events()
            self.ship.update()
            self._update_screen()


if __name__ == "__main__":
    pygame.init()

    # Make a game instance, and run the game.
    try:
        Game().run()
    finally:
        pygame.quit()
