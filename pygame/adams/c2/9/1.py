"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

The need of having a break
"""
import pygame
from enemy import Enemy
from bullet import Bullet

WIN_SIZE = (700, 200)
FPS = 30  # increase it to make the bug even more noticeable!
TITLE = "Bugged continuous fire"


class Game:
    BACKGROUND_COLOR = (200, 200, 200)

    def __init__(self, window: pygame.Window, screen: pygame.Surface) -> None:
        self.window = window
        self.screen = screen
        self.viewport = screen.get_rect()
        self.running = True

        self.enemy = Enemy(self.viewport)
        self.all_sprites = pygame.sprite.Group(self.enemy)

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

    def update(self, dt: float) -> None:
        bullet = self.enemy.fire()  # !!! BUG: enemy fires once for frame !!!
        self.all_sprites.add(bullet)

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
