"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Mouse actions
"""

from typing import Any, Tuple
import pygame


class Ball(pygame.sprite.Sprite):
    FILENAME = "../images/blue_ball.png"
    DEFAULT_SCALE = 10

    def __init__(self) -> None:
        super().__init__()
        self.image_orig = pygame.image.load(Ball.FILENAME).convert_alpha()
        self.scale = Ball.DEFAULT_SCALE
        self.image: pygame.Surface = self.scale_image()
        self.rect: pygame.Rect = self.image.get_rect()

    def scale_image(self):
        return pygame.transform.scale(self.image_orig, (self.scale, self.scale))

    def update(self, *args: Any, **kwargs: Any) -> None:
        if "go" in kwargs.keys():
            if kwargs["go"]:
                self.rect.clamp_ip(Game.INNER_RECT)
                c = self.rect.center  # Store previous center
                self.image = self.scale_image()
                self.rect = self.image.get_rect()
                self.rect.center = c  # Reset center

        if "center" in kwargs.keys():
            self.set_center(kwargs["center"])

    def draw(self, screen: pygame.Surface) -> None:
        screen.blit(self.image, self.rect)

    def rotate(self, ccw: bool) -> None:
        angle = 90 * (1 if ccw else -1)
        self.image_orig = pygame.transform.rotate(self.image_orig, angle)

    def resize(self, delta: int) -> None:
        self.scale += delta
        if self.scale > Game.INNER_RECT.width:
            self.scale = Game.INNER_RECT.width
        elif self.scale < 5:
            self.scale = 5

    def set_center(self, center: Tuple[int, int]) -> None:
        self.rect.center = center


class Game:
    WIN_RECT = pygame.Rect(0, 0, 600, 600)
    TITLE = "Dealing with mouse events"
    INNER_RECT = pygame.Rect(100, 100, WIN_RECT.width - 200, WIN_RECT.height - 200)
    BACKGROUND_COLOR = "white"
    INNER_BORDER_COLOR = "red"
    FPS = 30
    DELTATIME = 1.0 / FPS

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
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                match event.button:
                    case 1:
                        self.ball.rotate(True)
                    case 2:
                        return False
                    case 3:
                        self.ball.rotate(False)
                    case 4:
                        self.ball.resize(2)
                    case 5:
                        self.ball.resize(-2)
        return True

    def update(self):
        pos = pygame.mouse.get_pos()
        self.ball.update(center=pos)
        pygame.mouse.set_visible(not Game.INNER_RECT.collidepoint(pos))
        self.ball.update(go=True)

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
