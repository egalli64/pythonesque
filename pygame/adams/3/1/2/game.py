"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Exploding rocks
"""
import pygame
from timer import Timer
from rock import Rock

WIN_RECT = pygame.Rect(0, 0, 300, 200)


class Game(object):
    FPS = 30
    TITLE = "Exploding rocks"
    BACKGROUND_COLOR = "black"

    def __init__(self) -> None:
        self.window = pygame.Window(Game.TITLE, WIN_RECT.size)
        self.screen = self.window.get_surface()
        self.viewport = self.screen.get_rect()
        self.clock = pygame.time.Clock()

        self.all_rocks = pygame.sprite.Group()
        self.timer = Timer(500)

    def run(self) -> None:
        while self.handle_events():
            self.clock.tick(Game.FPS)

            if self.timer.tick():
                self.all_rocks.add(Rock(self.viewport))
            self.all_rocks.update()

            self.screen.fill(Game.BACKGROUND_COLOR)
            self.all_rocks.draw(self.screen)
            self.window.flip()

    def handle_events(self) -> bool:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
        return True


if __name__ == "__main__":
    pygame.init()

    try:
        Game().run()
    finally:
        pygame.quit()
        print("Done.")
