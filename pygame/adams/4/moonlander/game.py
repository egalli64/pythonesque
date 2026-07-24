"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Moon Lander
"""
import pygame

from sky import Sky
from moon import Moon
from lander import Lander
from question import Question

WIN_SIZE = (600, 800)
TITLE = "Moon Lander"


class Game:
    lander: Lander

    HORIZON_Y = 50
    FPS = 60

    def __init__(self, window: pygame.Window, screen: pygame.Surface) -> None:
        self.window = window
        self.screen = screen
        viewport = screen.get_rect()
        self.question = Question(viewport)
        self.sky = Sky(pygame.Rect(0, 0, viewport.width, viewport.height - Game.HORIZON_Y))
        self.moon = Moon(viewport, Game.HORIZON_Y)
        self.active = True
        self.running = True

    def run(self) -> None:
        self.restart()
        clock = pygame.time.Clock()

        while self.running:
            dt = clock.tick(Game.FPS) / 1000

            self.handle_events()
            self.update(dt)
            self.draw()

    def handle_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.WINDOWCLOSE:
                self.running = False
            elif event.type == Lander.EVENT_LANDED:
                self.active = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False

                if self.active:
                    if event.key == pygame.K_h:
                        self.lander.toggle_auto()
                else:
                    if event.key == pygame.K_q:
                        self.running = False
                    elif event.key == pygame.K_r:
                        self.restart()

        if self.active:
            keys = pygame.key.get_pressed()
            self.lander.thrust(keys[pygame.K_SPACE])

    def update(self, dt) -> None:
        self.sky.update()
        self.lander.update(dt)

    def draw(self) -> None:
        self.sky.draw(self.screen)
        self.moon.draw(self.screen)
        self.lander.draw()
        if not self.active:
            self.question.draw(self.screen)
        self.window.flip()

    def restart(self) -> None:
        self.active = True
        self.lander = Lander(self.window, Game.HORIZON_Y)


if __name__ == "__main__":
    pygame.init()
    pg_window = pygame.Window(TITLE, WIN_SIZE, pygame.WINDOWPOS_CENTERED)
    pg_screen = pg_window.get_surface()

    try:
        Game(pg_window, pg_screen).run()
    finally:
        pygame.quit()
        print("Done.")
