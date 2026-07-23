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


class Game:
    def __init__(self) -> None:
        self.window = pygame.Window(TITLE, WIN_RECT.size)
        self.screen = self.window.get_surface()
        viewport = self.screen.get_rect()
        self.clock = pygame.time.Clock()

        self.font = pygame.font.Font(None, 12)
        self.cat = Cat(viewport)
        self.cat_group = pygame.sprite.GroupSingle(self.cat)

    def run(self) -> None:
        while self.handle_events():
            dt = self.clock.tick(FPS) / 1000

            self.cat.update(dt)
            self.draw()

    def handle_events(self) -> bool:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
                elif event.key == pygame.K_PLUS:
                    self.cat.animation.change_duration(False)
                elif event.key == pygame.K_MINUS:
                    self.cat.animation.change_duration(True)
        return True

    def draw(self) -> None:
        self.screen.fill(BACKGROUND_COLOR)
        self.cat_group.draw(self.screen)
        text = f"animation time: {self.cat.animation.duration:.2f}"
        caption = self.font.render(text, True, TEXT_COLOR)
        text_rect = caption.get_rect()
        text_rect.centerx = WIN_RECT.centerx
        text_rect.bottom = WIN_RECT.bottom - 50
        self.screen.blit(caption, text_rect)
        self.window.flip()


if __name__ == "__main__":
    pygame.init()

    try:
        Game().run()
    finally:
        pygame.quit()
        print("Done.")
