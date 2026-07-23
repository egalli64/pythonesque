"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Colliding rocks
"""
import pygame

from timer import Timer
from rock import Rock
from explosion import Explosion

WIN_SIZE = (300, 200)
FPS = 30
TITLE = "Colliding rocks"
BACKGROUND_COLOR = "black"


class Game:
    def __init__(self, window: pygame.Window, screen: pygame.Surface) -> None:
        self.window = window
        self.screen = screen
        self.viewport = self.screen.get_rect()

        self.all_rocks: pygame.sprite.Group[Rock] = pygame.sprite.Group[Rock]()
        self.timer = Timer(500)
        self.running = True

    def run(self) -> None:
        clock = pygame.time.Clock()
        while self.running:
            dt = clock.tick(FPS) / 1000

            self.handle_events()
            self.update(dt)

            self.screen.fill(BACKGROUND_COLOR)
            self.all_rocks.draw(self.screen)
            self.window.flip()

    def handle_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False

    def update(self, dt) -> None:
        if self.timer.tick():
            self.all_rocks.add(Rock(self.viewport))
        self.all_rocks.update(dt)

        rocks = self.all_rocks.sprites()
        for i in range(len(rocks)):
            for j in range(i + 1, len(rocks)):
                if pygame.sprite.collide_rect(rocks[i], rocks[j]):
                    rocks[i].explode()
                    rocks[j].explode()


# noinspection DuplicatedCode
if __name__ == "__main__":
    pygame.init()
    pg_window = pygame.Window(TITLE, WIN_SIZE)
    pg_screen = pg_window.get_surface()

    Explosion.load_resources()
    Rock.load_resources()

    try:
        Game(pg_window, pg_screen).run()
    finally:
        pygame.quit()
        print("Done.")
