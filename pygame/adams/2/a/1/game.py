"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Mouse actions
"""
import pygame
from ball import Ball

WIN_SIZE = (600, 600)


class Game:
    TITLE = "Dealing with mouse events"
    INNER_RECT = pygame.Rect(100, 100, 400, 400)
    BACKGROUND_COLOR = "white"
    INNER_BORDER_COLOR = "red"
    FPS = 30

    def __init__(self, window: pygame.Window, screen: pygame.Surface) -> None:
        self.window = window
        self.screen = screen
        self.running = True

        self.ball = Ball(Game.INNER_RECT)
        self.group = pygame.sprite.GroupSingle(self.ball)

    def run(self) -> None:
        clock = pygame.time.Clock()

        while self.running:
            clock.tick(Game.FPS)

            self.handle_events()
            self.update()
            self.draw()

    def handle_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                match event.button:
                    case 1:  # LEFT
                        self.ball.rotate(counterclockwise=True)
                    case 2:  # MIDDLE
                        self.running = False
                    case 3:  # RIGHT
                        self.ball.rotate(counterclockwise=False)
            elif event.type == pygame.MOUSEWHEEL:  # previously known as button 4 and 5
                self.ball.resize(event.y)

    def update(self) -> None:
        pos = pygame.mouse.get_pos()
        if Game.INNER_RECT.collidepoint(pos):
            pygame.mouse.set_visible(False)
            self.ball.update(pos)
        else:
            pygame.mouse.set_visible(True)

    def draw(self) -> None:
        self.screen.fill(self.BACKGROUND_COLOR)
        pygame.draw.rect(self.screen, Game.INNER_BORDER_COLOR, Game.INNER_RECT, 1)
        self.group.draw(self.screen)
        self.window.flip()


if __name__ == "__main__":
    pygame.init()
    pg_window = pygame.Window(Game.TITLE, WIN_SIZE)
    pg_screen = pg_window.get_surface()

    Ball.load_resources()

    try:
        Game(pg_window, pg_screen).run()
    finally:
        pygame.quit()
        print("Done.")
