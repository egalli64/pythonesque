"""
A few simple PyGame apps: https://github.com/egalli64/pythonesque/ pygame/my folder

An Object-Oriented Hello PyGame app
"""
import pygame

TITLE = "Objectified Hello"
WIN_SIZE = (300, 300)
FPS = 30
BACKGROUND_COLOR = "blue"


class Game:
    def __init__(self, window: pygame.Window, screen: pygame.Surface) -> None:
        self.window = window
        self.screen = screen
        self.viewport = screen.get_rect()
        self.running = True

    def run(self) -> None:
        clock = pygame.time.Clock()

        while self.running:
            clock.tick(FPS)

            self.handle_events()
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

    def draw(self) -> None:
        self.screen.fill(BACKGROUND_COLOR)
        self.window.flip()


if __name__ == "__main__":
    pygame.init()
    main_window = pygame.Window(TITLE, WIN_SIZE)
    main_surface = main_window.get_surface()

    try:
        # Decoupling the Game object from the actual window and surface provider
        Game(main_window, main_surface).run()
    finally:
        pygame.quit()
