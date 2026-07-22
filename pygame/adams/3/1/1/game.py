"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

A running cat
"""
import pygame
from cat import Cat

WIN_SIZE = (300, 200)


class Game:
    FPS = 30
    TITLE = "Cat animation"
    BACKGROUND_COLOR = "gray"
    TEXT_COLOR = "white"

    def __init__(self, window: pygame.Window, screen: pygame.Surface) -> None:
        self.window = window
        self.screen = screen
        self.viewport = screen.get_rect()

        self.font = pygame.font.Font(None, 12)
        self.cat = Cat(self.viewport)
        self.cat_group = pygame.sprite.GroupSingle(self.cat)

    def run(self) -> None:
        clock = pygame.time.Clock()

        while self.handle_events():
            clock.tick(Game.FPS)

            self.cat.update()
            self.draw()

    def handle_events(self) -> bool:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
                elif event.key == pygame.K_PLUS:
                    self.cat.change_timing(-10)
                elif event.key == pygame.K_MINUS:
                    self.cat.change_timing(10)
        return True

    def draw(self) -> None:
        self.screen.fill(Game.BACKGROUND_COLOR)
        self.cat_group.draw(self.screen)
        text = f"animation time: {self.cat.animation.timer.duration}"
        caption = self.font.render(text, True, Game.TEXT_COLOR)
        text_rect = caption.get_rect(midbottom=(self.viewport.centerx, self.viewport.bottom - 50))
        self.screen.blit(caption, text_rect)
        self.window.flip()


if __name__ == "__main__":
    pygame.init()
    pg_window = pygame.Window(Game.TITLE, WIN_SIZE)
    pg_screen = pg_window.get_surface()

    try:
        Game(pg_window, pg_screen).run()
    finally:
        pygame.quit()
        print("Done.")
