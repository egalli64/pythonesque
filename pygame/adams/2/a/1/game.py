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

    def __init__(self) -> None:
        self.window = pygame.Window(Game.TITLE, WIN_SIZE)
        self.screen = self.window.get_surface()
        self.clock = pygame.time.Clock()

        self.ball = Ball(Game.INNER_RECT)

    def run(self) -> None:
        while self.handle_events():
            self.clock.tick(Game.FPS)
            self.update()
            self.draw()

    def handle_events(self) -> bool:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                match event.button:
                    case 1:  # LEFT
                        self.ball.rotate(True)
                    case 2:  # MIDDLE
                        return False
                    case 3:  # RIGHT
                        self.ball.rotate(False)
            elif event.type == pygame.MOUSEWHEEL:  # previously known as button 4 and 5
                self.ball.resize(event.y)
        return True

    def update(self):
        pos = pygame.mouse.get_pos()
        pygame.mouse.set_visible(not Game.INNER_RECT.collidepoint(pos))
        self.ball.update(pos)

    def draw(self) -> None:
        self.screen.fill(self.BACKGROUND_COLOR)
        pygame.draw.rect(self.screen, Game.INNER_BORDER_COLOR, Game.INNER_RECT, 1)
        self.ball.draw(self.screen)
        self.window.flip()


if __name__ == "__main__":
    pygame.init()

    try:
        Game().run()
    finally:
        pygame.quit()
        print("Done.")
