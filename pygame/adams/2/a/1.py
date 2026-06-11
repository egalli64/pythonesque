"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Mouse actions
"""

from typing import Tuple, override
import pygame


class Ball(pygame.sprite.Sprite):
    FILENAME = "../images/blue_ball.png"
    MIN_SIZE = 10
    MAX_SIZE = 400

    def __init__(self) -> None:
        super().__init__()
        self.image_base = pygame.image.load(Ball.FILENAME).convert_alpha()
        self.size = Ball.MIN_SIZE
        self.image: pygame.Surface = self.scale()
        self.rect: pygame.Rect = self.image.get_rect()

    def scale(self):
        self.dirty = False
        return pygame.transform.scale(self.image_base, (self.size, self.size))

    @override
    def update(self, pos) -> None:
        self.set_center(pos)
        self.rect.clamp_ip(Game.INNER_RECT)
        if self.dirty:
            center = self.rect.center
            self.image = self.scale()
            self.rect = self.image.get_rect()
            self.rect.center = center

    def draw(self, screen: pygame.Surface) -> None:
        screen.blit(self.image, self.rect)

    def rotate(self, ccw: bool) -> None:
        self.dirty = True
        angle = 90 * (1 if ccw else -1)
        self.image_base = pygame.transform.rotate(self.image_base, angle)

    def resize(self, delta: int) -> None:
        if Ball.MIN_SIZE <= self.size + delta <= Ball.MAX_SIZE:
            self.size += delta
            self.dirty = True

    def set_center(self, center: Tuple[int, int]) -> None:
        self.rect.center = center


class Game:
    INNER_RECT = pygame.Rect(100, 100, Ball.MAX_SIZE, Ball.MAX_SIZE)
    WIN_RECT = pygame.Rect(0, 0, INNER_RECT.width + 200, INNER_RECT.height + 200)
    TITLE = "Dealing with mouse events"
    BACKGROUND_COLOR = "white"
    INNER_BORDER_COLOR = "red"
    FPS = 30

    def __init__(self) -> None:
        self.window = pygame.Window(Game.TITLE, Game.WIN_RECT.size)
        self.screen = self.window.get_surface()
        self.clock = pygame.time.Clock()

        self.ball = Ball()

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
