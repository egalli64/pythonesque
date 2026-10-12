"""
A few simple PyGame apps: https://github.com/egalli64/pythonesque/ pygame/my folder

A traffic light
"""
import pygame

TITLE = "Stop!"
WIN_SIZE = (200, 300)
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

        cx = WIN_SIZE[0] / 2  # Central X

        # The pole
        pygame.draw.line(self.screen, "grey", (cx, 240), (cx, 280), width=10)
        # The main body
        pygame.draw.rect(self.screen, "black", (65, 60, 70, 180), border_radius=6)
        # The lights
        pygame.draw.circle(self.screen, "red", (cx, 95), 25)
        pygame.draw.circle(self.screen, "darkgrey", (cx, 95), 25, width=2)
        pygame.draw.circle(self.screen, "yellow", (cx, 150), 25)
        pygame.draw.circle(self.screen, "darkgrey", (cx, 150), 25, width=2)
        pygame.draw.circle(self.screen, "green", (cx, 205), 25)
        pygame.draw.circle(self.screen, "darkgrey", (cx, 205), 25, width=2)

        self.window.flip()


if __name__ == "__main__":
    pygame.init()
    main_window = pygame.Window(TITLE, WIN_SIZE)
    main_surface = main_window.get_surface()

    try:
        Game(main_window, main_surface).run()
    finally:
        pygame.quit()
