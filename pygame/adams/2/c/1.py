"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Printing events
"""

import pygame


class Game:
    WIN_RECT = pygame.Rect(0, 0, 600, 300)
    TITLE = "Printing events"
    BACKGROUND_COLOR = "white"
    FPS = 30

    def __init__(self) -> None:
        pygame.init()
        self.window = pygame.Window(Game.TITLE, Game.WIN_RECT.size)
        self.screen = self.window.get_surface()
        self.clock = pygame.time.Clock()
        self.running = True

    def run(self) -> None:
        while self.handle_events():
            self.clock.tick(Game.FPS)
            self.screen.fill(self.BACKGROUND_COLOR)
            self.window.flip()

    def handle_events(self) -> bool:
        for event in pygame.event.get():
            print(event)  # Print event information
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
