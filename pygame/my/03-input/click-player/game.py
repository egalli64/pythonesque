"""
My PyGame CE tutorial: https://github.com/egalli64/pythonesque/ pygame/my folder

User input: Mouse events
"""
import pygame
from player import Player

TITLE = "Mouse events"
WIN_SIZE = (400, 300)
FPS = 60
BACKGROUND_COLOR = "green"


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
                case pygame.MOUSEBUTTONDOWN:
                    match event.button:
                        case pygame.BUTTON_LEFT:
                            # support dynamic window resizing
                            self.player.move_to(event.pos, self.viewport)
                        case pygame.BUTTON_RIGHT:
                            self.player.change_color()
                case pygame.MOUSEWHEEL:
                    self.player.change_radius(event.y)

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
