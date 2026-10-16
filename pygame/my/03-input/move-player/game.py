"""
My PyGame CE tutorial: https://github.com/egalli64/pythonesque/ pygame/my folder

User input: Keyboard Continuous Polling (classy)
"""
import pygame
from player import Player

TITLE = "Objectified Continuous Polling"
WIN_SIZE = (400, 300)
FPS = 60
BACKGROUND_COLOR = "whitesmoke"


class Game:
    def __init__(self, window: pygame.Window, screen: pygame.Surface) -> None:
        self.window = window
        self.screen = screen
        self.viewport = self.screen.get_rect()
        self.running = True

        self.player = Player()

    def run(self) -> None:
        clock = pygame.time.Clock()

        while self.running:
            clock.tick(FPS)

            self.handle_events()
            self.update()
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

        keys = pygame.key.get_pressed()
        self.player.set_direction(keys)

    def update(self) -> None:
        self.player.update(self.viewport)

    def draw(self) -> None:
        self.screen.fill(BACKGROUND_COLOR)
        self.player.draw(self.screen)

        self.window.flip()


if __name__ == "__main__":
    pygame.init()
    main_window = pygame.Window(TITLE, WIN_SIZE)
    main_surface = main_window.get_surface()

    try:
        Game(main_window, main_surface).run()
    finally:
        pygame.quit()
