"""
A few simple PyGame apps: https://github.com/egalli64/pythonesque/ pygame/my folder

Basic shapes
"""
import pygame

TITLE = "Basic shapes"
WIN_SIZE = (260, 160)
FPS = 30
BACKGROUND_COLOR = "whitesmoke"


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

        pygame.draw.rect(self.screen, "red", pygame.Rect(10, 10, 40, 60))  # rectangle: left, top, width, height
        pygame.draw.polygon(self.screen, "blue", ((80, 10), (140, 10), (160, 70), (60, 70)))  # point: x, y
        pygame.draw.circle(self.screen, "yellow", center=(200, 40), radius=30)

        pygame.draw.line(self.screen, "green", start_pos=(250, 10), end_pos=(250, 150), width=3)
        pygame.draw.line(self.screen, "violet", start_pos=(10, 80), end_pos=(250, 80))

        pygame.draw.rect(self.screen, "chocolate", pygame.Rect(10, 90, 40, 60), width=2, border_radius=4)
        pygame.draw.polygon(self.screen, "purple", ((80, 90), (140, 90), (160, 150), (60, 150)), width=1)
        pygame.draw.circle(self.screen, "magenta", center=(200, 120), radius=30, width=2)

        self.window.flip()


if __name__ == "__main__":
    pygame.init()
    main_window = pygame.Window(TITLE, WIN_SIZE)
    main_surface = main_window.get_surface()

    try:
        Game(main_window, main_surface).run()
    finally:
        pygame.quit()
