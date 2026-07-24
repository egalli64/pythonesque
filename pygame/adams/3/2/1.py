"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Extract a tile from a tileset
"""
import pygame

TILE = pygame.math.Vector2(32, 32)
SHEET = (16, 12)
WIN_SIZE = (SHEET[0] * TILE.x, SHEET[1] * TILE.y)
TITLE = "A Meadow"
FPS = 30


class Meadow:
    @classmethod
    def load_resources(cls) -> None:
        tiles = pygame.image.load("../images/forest-tiles.png").convert_alpha()
        cls._image = tiles.subsurface(pygame.Rect((0, 0), TILE))

    def __init__(self, screen: pygame.Surface) -> None:
        self.screen = screen

    def draw(self) -> None:
        self.screen.fill("black")
        for row in range(SHEET[1]):
            for col in range(SHEET[0]):
                position = col * TILE.x, row * TILE.y
                self.screen.blit(Meadow._image, position)


class Game:
    def __init__(self, window: pygame.Window, screen: pygame.Surface) -> None:
        self.window = window
        self.meadow = Meadow(screen)
        self.running = True

    def run(self) -> None:
        clock = pygame.time.Clock()
        while self.running:
            clock.tick(FPS)

            self.handle_events()
            self.meadow.draw()
            self.window.flip()

    def handle_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False


if __name__ == "__main__":
    pygame.init()
    pg_window = pygame.Window(TITLE, WIN_SIZE)
    pg_screen: pygame.Surface = pg_window.get_surface()

    Meadow.load_resources()

    try:
        Game(pg_window, pg_screen).run()
    finally:
        pygame.quit()
        print("Done.")
