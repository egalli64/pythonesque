"""
Python Crash Course, Third Edition, Part II https://nostarch.com/python-crash-course-3rd-edition
My notes: https://github.com/egalli64/pythonesque/ pygame/pcc3 folder

Chapter 14 - Scoring
Leveling up
"""

from time import sleep
import pygame

from ship import Ship
from bullet import Bullet
from alien import Alien
from button import Button


class Game:
    """Overall class to manage game assets and behavior."""

    NAME = "Alien Invasion"
    FPS = 30

    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    SCREEN_SIZE = pygame.Vector2(SCREEN_WIDTH, SCREEN_HEIGHT)

    BACKGROUND_COLOR = (230, 230, 230)  # light gray

    SHIP_COUNT = 3
    MAX_BURST_SIZE = 3

    FLEET_DROP_SPEED = 10

    DEFAULT_BULLET_SPEED = 2

    # How quickly the game speeds up
    SPEEDUP_SCALE = 1.3

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(Game.SCREEN_SIZE)
        pygame.display.set_caption(Game.NAME)

        self.ship = Ship(self.screen)
        self.ships_left = Game.SHIP_COUNT
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self.active = False
        # Make the Play button.
        self.play_button = Button(self, "Play")

        self._create_fleet()

    def setup(self):
        """Any time a new fleet is ready to invade"""
        self.bullet_speed = Game.DEFAULT_BULLET_SPEED
        Alien.speed = Alien.DEFAULT_SPEED
        Alien.fleet_direction = 1

    def increase_speed(self):
        """Increase speed settings."""
        self.ship.speed *= Game.SPEEDUP_SCALE
        self.bullet_speed *= Game.SPEEDUP_SCALE
        Alien.speed *= Game.SPEEDUP_SCALE

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
            alien.rect.y += Game.FLEET_DROP_SPEED
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
        while pos.y < (Game.SCREEN_SIZE.y - 3 * alien_size.y):
            while pos.x < (Game.SCREEN_SIZE.x - 2 * alien_size.x):
                self._create_alien(*pos)
                pos.x += 2 * alien_size.x

            # Finished a row; reset x value, and increment y value.
            pos.x = alien_size.x
            pos.y += 2 * alien_size.y

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < Game.MAX_BURST_SIZE:
            bullet = Bullet(self.screen, self.ship.rect, self.bullet_speed)
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
        """Respond to keyup events - a keyup is never terminating"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks Play."""
        if not self.active and self.play_button.rect.collidepoint(mouse_pos):
            self.setup()
            self.ships_left = Game.SHIP_COUNT
            self.active = True

            # Get rid of any remaining bullets and aliens.
            self.bullets.empty()
            self.aliens.empty()

            # Create a new fleet and center the ship.
            self._create_fleet()
            self.ship.setup()

            # Hide the mouse cursor.
            pygame.mouse.set_visible(False)

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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

        return True

    def _ship_hit(self):
        """Respond to the ship being hit by an alien."""
        self.ships_left -= 1

        if self.ships_left > 0:
            # Get rid of any remaining bullets and aliens.
            self.bullets.empty()
            self.aliens.empty()
            # Create a new fleet and center the ship.
            self._create_fleet()
            self.increase_speed()
            self.ship.setup()

            sleep(0.5)
        else:
            self.active = False
            pygame.mouse.set_visible(True)

    def _check_aliens_bottom(self):
        """Check if any aliens have reached the bottom of the screen."""
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= Game.SCREEN_SIZE.y:
                # Treat this the same as if the ship got hit.
                self._ship_hit()
                break

    def _update_aliens(self):
        """Check if the fleet is at an edge, then update positions."""
        self._check_fleet_edges()
        self.aliens.update()
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        # Look for aliens hitting the bottom of the screen.
        self._check_aliens_bottom()

    def _update_bullets(self):
        """Update position of bullets and check for alien collision"""
        self.bullets.update()
        pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()

    def _update_screen(self):
        """Redraw the screen during each pass through the loop"""
        self.screen.fill(Game.BACKGROUND_COLOR)
        self.ship.blit()
        for bullet in self.bullets.sprites():
            bullet.draw()

        self.aliens.draw(self.screen)

        # Draw the play button if the game is inactive.
        if not self.active:
            self.play_button.draw_button()

        # Make the most recently drawn screen visible.
        pygame.display.flip()

    def run(self):
        """The game main loop"""
        while self._check_events():
            if self.active:
                self.ship.update()
                self._update_aliens()
                self._update_bullets()

            self._update_screen()
            self.clock.tick(Game.FPS)


if __name__ == "__main__":
    # Make a game instance, and run the game.
    game = Game()
    game.run()

    print("Done.")
