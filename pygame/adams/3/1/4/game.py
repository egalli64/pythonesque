"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

A running cat - dt from main loop
"""
import pygame
from cat import Cat

WIN_RECT = pygame.Rect(0, 0, 300, 200)
TITLE = "Cat animation"
FPS = 30
BACKGROUND_COLOR = "gray"
TEXT_COLOR = "white"
FONT_SIZE = 14


class Game:
    @classmethod
    def load_resources(cls) -> None:
        cls._font = pygame.font.Font(None, FONT_SIZE)

    def __init__(self, window: pygame.Window, screen: pygame.Surface) -> None:
        self.window = window
        self.screen = screen
        self.viewport = self.screen.get_rect()

        self.cat = Cat(self.viewport)
        self.cat_group = pygame.sprite.GroupSingle(self.cat)
        self.running = True

    def run(self) -> None:
        clock = pygame.time.Clock()

        while self.running:
            dt = clock.tick(FPS) / 1000

            self.handle_events()
            self.cat.update(dt)
            self.draw()

    def handle_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                elif event.key == pygame.K_PLUS:
                    self.cat.change_duration(False)
                elif event.key == pygame.K_MINUS:
                    self.cat.change_duration(True)

    def draw(self) -> None:
        self.screen.fill(BACKGROUND_COLOR)
        self.cat_group.draw(self.screen)

        text = f"animation time: {self.cat.duration:.2f}"
        caption = Game._font.render(text, True, TEXT_COLOR)
        center = (self.viewport.centerx, self.viewport.centery - 50)
        text_rect = caption.get_rect(center=center)
        self.screen.blit(caption, text_rect)
        self.window.flip()


# noinspection DuplicatedCode
if __name__ == "__main__":
    pygame.init()
    pg_window = pygame.Window(TITLE, WIN_RECT.size)
    pg_screen = pg_window.get_surface()

    Game.load_resources()
    Cat.load_resources()

    try:
        Game(pg_window, pg_screen).run()
    finally:
        pygame.quit()
        print("Done.")
