"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Colliding rocks
"""
import pygame
from timer import Timer
from rock import Rock

WIN_SIZE = (300, 200)


class Game:
    FPS = 30
    TITLE = "Colliding rocks"
    BACKGROUND_COLOR = "black"

    def __init__(self) -> None:
        self.window = pygame.Window(Game.TITLE, WIN_SIZE)
        self.screen = self.window.get_surface()
        self.viewport = self.screen.get_rect()
        self.clock = pygame.time.Clock()

        self.all_rocks: pygame.sprite.Group[Rock] = pygame.sprite.Group[Rock]()
        self.timer = Timer(500)

    def run(self) -> None:
        while self.handle_events():
            dt = self.clock.tick(Game.FPS) / 1000

            self.update(dt)

            self.screen.fill(self.BACKGROUND_COLOR)
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


if __name__ == "__main__":
    pygame.init()

    try:
        Game().run()
    finally:
        pygame.quit()
        print("Done.")
