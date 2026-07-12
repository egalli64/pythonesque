"""
A few simple PyGame apps: https://github.com/egalli64/pythonesque/ pygame/my folder

Bouncing Ball
"""
import pygame
from ball import Ball

WIN_SIZE = (800, 600)
TITLE = "Bouncing Ball"
BACKGROUND_COLOR = "black"
FPS = 60


class Game:
    def __init__(self, window: pygame.Window, screen: pygame.Surface) -> None:
        self.window = window
        self.screen = screen
        self.running = True

        rect = screen.get_rect()
        self.ball = Ball(rect.center)

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
        self.ball.update(dt)

    def draw(self):
        self.screen.fill(BACKGROUND_COLOR)
        self.ball.draw(self.screen)
        self.window.flip()


if __name__ == "__main__":
    pygame.init()
    pg_window = pygame.Window(TITLE, WIN_SIZE)
    pg_screen = pg_window.get_surface()

    try:
        Game(pg_window, pg_screen).run()
    finally:
        pygame.quit()
        print("Done.")
