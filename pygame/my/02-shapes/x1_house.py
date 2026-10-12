"""
A few simple PyGame apps: https://github.com/egalli64/pythonesque/ pygame/my folder

A little house
"""
import pygame

TITLE = "A little house"
WIN_SIZE = (260, 160)
FPS = 30


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
        # Background
        self.screen.fill("skyblue")
        # Ground (rectangle at the bottom)
        pygame.draw.rect(self.screen, "forestgreen", pygame.Rect(0, 120, 260, 40))
        # Sun (circle in the top-right corner)
        pygame.draw.circle(self.screen, "gold", center=(220, 40), radius=25)
        # House Body (rectangle)
        pygame.draw.rect(self.screen, "firebrick", pygame.Rect(70, 70, 100, 60))
        # Roof (triangle)
        pygame.draw.polygon(self.screen, "midnightblue", ((60, 70), (120, 25), (180, 70)))
        # Door (rectangle)
        pygame.draw.rect(self.screen, "saddlebrown", pygame.Rect(110, 95, 20, 35))

        self.window.flip()


if __name__ == "__main__":
    pygame.init()
    main_window = pygame.Window(TITLE, WIN_SIZE)
    main_surface = main_window.get_surface()

    try:
        Game(main_window, main_surface).run()
    finally:
        pygame.quit()
