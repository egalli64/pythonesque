"""
A few simple PyGame apps: https://github.com/egalli64/pythonesque/ pygame/my folder

One-shot event - press space on keyboard to change the background color
"""
import pygame

TITLE = "One-Shot Event"
WIN_SIZE = (300, 200)
FPS = 30
COLORS = ["beige", "lightblue", "peachpuff", "thistle"]


class Game:
    def __init__(self, window: pygame.Window, screen: pygame.Surface) -> None:
        self.window = window
        self.screen = screen
        self.running = True

        self.color_index = 0

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
                        case pygame.K_SPACE:
                            # switch to the next background color
                            self.color_index = (self.color_index + 1) % len(COLORS)

    def draw(self) -> None:
        # dynamic background color - see K_SPACE event handling
        self.screen.fill(COLORS[self.color_index])
        self.window.flip()


if __name__ == "__main__":
    pygame.init()
    main_window = pygame.Window(TITLE, WIN_SIZE)
    main_surface = main_window.get_surface()

    try:
        Game(main_window, main_surface).run()
    finally:
        pygame.quit()
