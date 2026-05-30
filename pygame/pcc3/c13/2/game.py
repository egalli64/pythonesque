"""
Python Crash Course, Third Edition, Part II https://nostarch.com/python-crash-course-3rd-edition
My notes: https://github.com/egalli64/pythonesque/ pygame/pcc3 folder

Chapter 13 - Aliens!
Making the Fleet Move
"""

import pygame

from ship import Ship
from bullet import Bullet, BULLETS_ALLOWED
from alien import Alien

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
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

    def _create_alien(self, x, y):
        """Create an alien and place it in the row."""
        alien = Alien(self.screen)
        alien.x = x
        alien.rect.x = x
        alien.rect.y = y
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += Alien.FLEET_DROP_SPEED
        Alien.fleet_direction *= -1

    def _create_fleet(self):
        """
        Create the fleet of aliens

        Spacing between aliens is one alien width and one alien height
        """
        first_alien = Alien(self.screen)
        self.aliens.add(first_alien)

        alien_size = pygame.Vector2(first_alien.rect.size)

        pos = alien_size.copy()
        while pos.y < (SCREEN_HEIGHT - 3 * alien_size.y):
            while pos.x < (SCREEN_WIDTH - 2 * alien_size.x):
                self._create_alien(*pos)
                pos.x += 2 * alien_size.x

            # Finished a row; reset x value, and increment y value.
            pos.x = alien_size.x
            pos.y += 2 * alien_size.y

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < BULLETS_ALLOWED:
            bullet = Bullet(self.screen, self.ship.rect)
            self.bullets.add(bullet)

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
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

        return True

    def _check_keyup_events(self, event):
        """
        Respond to keyup events - a keyup is never terminating
        """
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

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
                self._check_keyup_events(event)

        return True

    def _update_aliens(self):
        """Check if the fleet is at an edge, then update positions."""
        self._check_fleet_edges()
        self.aliens.update()

    def _update_screen(self):
        """Redraw the screen during each pass through the loop"""
        self.screen.fill(BACKGROUND_COLOR)
        self.ship.blit()
        for bullet in self.bullets.sprites():
            bullet.draw()

        self.aliens.draw(self.screen)

        # Make the most recently drawn screen visible.
        pygame.display.flip()

    def run(self):
        """The game main loop"""
        while self._check_events():
            self.ship.update()
            self.bullets.update()
            self._update_aliens()

            self._update_screen()
            self.clock.tick(FPS)


if __name__ == "__main__":
    # Make a game instance, and run the game.
    game = Game()
    game.run()

    print("Done.")
