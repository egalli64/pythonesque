"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Exploding rocks
"""
import pygame
from timer import Timer
from rock import Rock

WIN_SIZE = (300, 200)
FPS = 30
TITLE = "Exploding rocks"
BACKGROUND_COLOR = "black"


class Game(object):
    def __init__(self, window: pygame.Window, screen: pygame.Surface) -> None:
        self.window = window
        self.screen = screen
        self.viewport = self.screen.get_rect()

        self.all_rocks = pygame.sprite.Group()
        self.timer = Timer(500)
        self.running = True

    def run(self) -> None:
        clock = pygame.time.Clock()
        while self.running:
            clock.tick(FPS)

            self.handle_events()

            if self.timer.tick():
                self.all_rocks.add(Rock(self.viewport))
            self.all_rocks.update()

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


# noinspection DuplicatedCode
if __name__ == "__main__":
    pygame.init()
    pg_window = pygame.Window(TITLE, WIN_SIZE)
    pg_screen = pg_window.get_surface()

    try:
        Game(pg_window, pg_screen).run()
    finally:
        pygame.quit()
        print("Done.")
