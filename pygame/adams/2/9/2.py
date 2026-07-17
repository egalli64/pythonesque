"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Timed continuous fire - Using time.get_ticks
"""
import pygame
from enemy import Enemy
from bullet import Bullet

WIN_SIZE = (700, 200)
FPS = 30
TITLE = "Timed continuous fire"


class Game:
    FIRE_INTERVAL = 333  # ms.
    BACKGROUND_COLOR = (200, 200, 200)

    def __init__(self, window: pygame.Window, screen: pygame.Surface) -> None:
        self.window = window
        self.screen = screen
        self.viewport = screen.get_rect()
        self.running = True

        self.enemy = Enemy(self.viewport)
        self.all_sprites = pygame.sprite.Group(self.enemy)
        self.last_shot_time = 0

    def run(self) -> None:
        clock = pygame.time.Clock()

        while self.running:
            dt = clock.tick(FPS) / 1000

            self.handle_events()
            self.update(dt)
            self.draw()

    def handle_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False

    def try_fire(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_shot_time >= Game.FIRE_INTERVAL:
            self.all_sprites.add(self.enemy.fire())
            self.last_shot_time = current_time

    def update(self, dt: float) -> None:
        self.try_fire()
        self.all_sprites.update(dt)

    def draw(self) -> None:
        self.screen.fill(Game.BACKGROUND_COLOR)
        self.all_sprites.draw(self.screen)
        self.window.flip()


# noinspection DuplicatedCode
if __name__ == "__main__":
    pygame.init()
    pg_window = pygame.Window(TITLE, WIN_SIZE)
    pg_screen = pg_window.get_surface()

    Enemy.load_resources()
    Bullet.load_resources()

    try:
        Game(pg_window, pg_screen).run()
    finally:
        pygame.quit()
        print("Done.")
