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

WIN_RECT = pygame.Rect(0, 0, 600, 800)
TITLE = "Moon Lander"


class Game:
    lander: Lander

    HORIZON_Y = 50
    FPS = 60

    def __init__(self, window: pygame.Window, screen: pygame.Surface) -> None:
        self.window = window
        self.screen = screen
        self.question = Question(WIN_RECT)
        self.sky = Sky(pygame.Rect(0, 0, WIN_RECT.width, WIN_RECT.height - Game.HORIZON_Y))
        self.moon = Moon(WIN_RECT, Game.HORIZON_Y)
        self.active = True

    def run(self) -> None:
        self.restart()
        clock = pygame.time.Clock()
        while self.handle_events():
            self.update()
            self.draw()
            clock.tick(Game.FPS)

    def handle_events(self) -> bool:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.WINDOWCLOSE:
                return False
            elif event.type == Lander.EVENT_LANDED:
                self.active = False
                self.lander.update(mode="landed", velocity=event.velocity)
            elif event.type == Lander.EVENT_CRASHED:
                self.active = False
                self.lander.update(mode="crashed", velocity=event.velocity)
            elif event.type == pygame.KEYDOWN:
                if self.active:
                    if event.key == pygame.K_h:
                        self.lander.update(action="toggle_ai")
                else:
                    if event.key == pygame.K_q:
                        return False
                    elif event.key == pygame.K_r:
                        self.restart()
                if event.key == pygame.K_ESCAPE:
                    return False

        if self.active:
            keys = pygame.key.get_pressed()
            self.lander.thrust(keys[pygame.K_SPACE])

        return True

    def update(self) -> None:
        self.sky.update()
        self.lander.update(action="move")

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
    pg_window = pygame.Window(TITLE, WIN_RECT.size, pygame.WINDOWPOS_CENTERED)
    pg_screen = pg_window.get_surface()

    try:
        Game(pg_window, pg_screen).run()
    finally:
        pygame.quit()
        print("Done.")
