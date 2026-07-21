"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Printing events
"""
import pygame

WIN_SIZE = (600, 300)
TITLE = "Printing events"
BACKGROUND_COLOR = "white"
FPS = 30


class Game:
    def __init__(self, window: pygame.Window, screen: pygame.Surface) -> None:
        self.window = window
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.running = True

    def run(self) -> None:
        while self.running:
            self.clock.tick(FPS)

            self.handle_events()
            self.screen.fill(BACKGROUND_COLOR)
            self.window.flip()

    def handle_events(self) -> None:
        for event in pygame.event.get():
            print(f"Event {pygame.event.event_name(event.type)} with attributes {event.dict}")

            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False


if __name__ == "__main__":
    pygame.init()
    pg_window = pygame.Window(TITLE, WIN_SIZE)
    pg_screen = pg_window.get_surface()

    try:
        Game(pg_window, pg_screen).run()
    finally:
        pygame.quit()
        print("Done.")
