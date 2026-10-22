"""
My PyGame CE tutorial: https://github.com/egalli64/pythonesque/ pygame/my folder

Text rendering: a more structured version
"""
import pygame

WIN_SIZE = (700, 200)
TITLE = "Text - structured"
BACKGROUND_COLOR = "whitesmoke"
FPS = 30

TEXT = "Hello, gamer!"
TEXT_COLOR = "black"
FONT_SIZE = 32


class Game:
    @classmethod
    def load_resources(cls) -> None:
        cls._font = pygame.font.Font(None, FONT_SIZE)

    def __init__(self, window: pygame.Window, screen: pygame.Surface) -> None:
        self.window = window
        self.screen = screen

        self.text_surface = Game._font.render(TEXT, True, TEXT_COLOR)
        self.text_rect = self.text_surface.get_rect(center=screen.get_rect().center)

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
        self.screen.blit(self.text_surface, self.text_rect)
        self.window.flip()


if __name__ == "__main__":
    pygame.init()
    main_window = pygame.Window(TITLE, WIN_SIZE)
    main_surface = main_window.get_surface()

    Game.load_resources()

    try:
        Game(main_window, main_surface).run()
    finally:
        pygame.quit()
