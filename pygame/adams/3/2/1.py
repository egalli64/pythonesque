"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Extract a tile from a tileset
"""

import pygame


class Meadow:
    TITLE = "A Meadow"
    TILE = pygame.math.Vector2(32, 32)
    SHEET = (16, 12)
    WIN_RECT = pygame.Rect(0, 0, SHEET[0] * TILE.x, SHEET[1] * TILE.y)

    def __init__(self) -> None:
        self.window = pygame.Window(Meadow.TITLE, Meadow.WIN_RECT.size)
        self.screen: pygame.Surface = self.window.get_surface()
        self.spritelib = pygame.image.load("../images/forest-tiles.png").convert_alpha()
        self.rect = self.screen.get_frect()
        self.clock = pygame.time.Clock()

    def draw(self) -> None:
        self.screen.fill("black")
        image = self.spritelib.subsurface(pygame.Rect((0, 0), Meadow.TILE))
        for row in range(Meadow.SHEET[1]):
            for col in range(Meadow.SHEET[0]):
                position = col * Meadow.TILE.x, row * Meadow.TILE.y
                self.screen.blit(image, position)
        self.window.flip()


class Game:
    FPS = 30

    def __init__(self) -> None:
        self.clock = pygame.time.Clock()
        self.window = Meadow()
        self.running = True

    def run(self) -> None:
        while self.handle_events():
            self.clock.tick(Game.FPS)
            self.window.draw()

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
