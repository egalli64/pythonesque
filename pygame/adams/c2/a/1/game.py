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
    PLAY_AREA = pygame.Rect(100, 100, 400, 400)
    BACKGROUND_COLOR = "white"
    INNER_BORDER_COLOR = "red"
    FPS = 30

    def __init__(self, window: pygame.Window, screen: pygame.Surface) -> None:
        self.window = window
        self.screen = screen
        self.running = True

        self.ball = Ball(Game.PLAY_AREA)
        self.group = pygame.sprite.GroupSingle(self.ball)
        # inside the play are the mouse is invisible
        pygame.mouse.set_visible(False)

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
                    case pygame.BUTTON_LEFT:
                        self.ball.rotate(counterclockwise=True)
                    case pygame.BUTTON_MIDDLE:
                        self.running = False
                    case pygame.BUTTON_RIGHT:
                        self.ball.rotate(counterclockwise=False)
            # previously known as pygame.BUTTON_WHEELUP (4) and BUTTON_WHEELDOWN (5)
            elif event.type == pygame.MOUSEWHEEL:
                self.ball.resize(event.y)

    def update(self) -> None:
        pos = pygame.mouse.get_pos()
        if Game.PLAY_AREA.collidepoint(pos):
            if pygame.mouse.get_visible():
                pygame.mouse.set_visible(False)
            self.group.update(pos)
        elif not pygame.mouse.get_visible():
            pygame.mouse.set_visible(True)

    def draw(self) -> None:
        self.screen.fill(self.BACKGROUND_COLOR)
        pygame.draw.rect(self.screen, Game.INNER_BORDER_COLOR, Game.PLAY_AREA, 1)
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
