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
        self.viewport = screen.get_rect()
        self.running = True

        self.ball = Ball(self.viewport.center)

    def run(self) -> None:
        clock = pygame.time.Clock()

        while self.running:
            dt = clock.tick(FPS) / 1000

            self.handle_events()
            self.update(dt)
            self.draw()

    def handle_events(self) -> None:
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    self.running = False
                case pygame.KEYDOWN:
                    match event.key:
                        case pygame.K_ESCAPE:
                            self.running = False
                        case pygame.K_SPACE:
                            self.ball.change_color()
                        case pygame.K_UP:
                            self.ball.increase_speed()
                        case pygame.K_DOWN:
                            self.ball.decrease_speed()
                        case pygame.K_r:
                            self.ball.reset(self.viewport.center)

    def update(self, dt: float) -> None:
        self.ball.update(dt, self.viewport)

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
