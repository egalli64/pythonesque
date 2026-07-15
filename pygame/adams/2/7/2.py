"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Text as a Sprite
"""
from typing import override
import pygame

FPS = 30

WIN_SIZE = (400, 100)
WIN_POS = (10, 50)
BACKGROUND_COLOR = "cornsilk1"
TITLE = "Text"


class TextSprite(pygame.sprite.Sprite):
    TEXT = "Hello World!"
    MIN_FONT_SIZE = 10
    DEFAULT_FONT_SIZE = 24
    DEFAULT_COLOR = (0, 0, 255)

    image: pygame.Surface
    rect: pygame.Rect
    font: pygame.font.Font
    color_channels: list[int]
    size: int
    dirty: bool

    @classmethod
    def load_resources(cls):
        cls._fonts = {cls.DEFAULT_FONT_SIZE: pygame.font.Font(None, cls.DEFAULT_FONT_SIZE)}

    def __init__(self, pos: tuple[int, int]) -> None:
        super().__init__()

        self.pos = pos
        self.reset()

    def reset(self) -> None:
        self.size = TextSprite.DEFAULT_FONT_SIZE
        self.font = TextSprite._fonts[TextSprite.DEFAULT_FONT_SIZE]
        self.color_channels = list(TextSprite.DEFAULT_COLOR)
        self.dirty = True

    @property
    def color(self) -> tuple[int, int, int]:
        r, g, b = self.color_channels
        return r, g, b

    def render_text(self) -> None:
        self.image = self.font.render(TextSprite.TEXT, True, self.color_channels)
        self.rect = self.image.get_rect(center=self.pos)

        print(self.size, self.color)  # not meant to be in production code!
        self.dirty = False

    def change_size(self, step: int = 1) -> None:
        candidate = max(TextSprite.MIN_FONT_SIZE, self.size + step)
        if candidate == self.size:
            return

        self.size = candidate
        if self.size not in TextSprite._fonts:
            TextSprite._fonts[self.size] = pygame.font.Font(None, self.size)
        self.font = TextSprite._fonts[self.size]

        self.dirty = True

    def change_color(self, delta: tuple[int, int, int]) -> None:
        for i in range(3):
            self.color_channels[i] = (self.color_channels[i] + delta[i]) % 256
        self.dirty = True

    @override
    def update(self) -> None:
        if self.dirty:
            self.render_text()


def main(window: pygame.Window, screen: pygame.Surface):
    viewport = screen.get_rect()

    hello = TextSprite(viewport.center)
    group = pygame.sprite.GroupSingle(hello)

    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_SPACE:
                    hello.reset()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_KP_PLUS] or keys[pygame.K_PLUS]:
            hello.change_size(+1)
        if keys[pygame.K_KP_MINUS] or keys[pygame.K_MINUS]:
            hello.change_size(-1)

        step = -1 if keys[pygame.K_LSHIFT] else 1
        if keys[pygame.K_r]:
            hello.change_color((step, 0, 0))
        if keys[pygame.K_g]:
            hello.change_color((0, step, 0))
        if keys[pygame.K_b]:
            hello.change_color((0, 0, step))

        group.update()

        screen.fill(BACKGROUND_COLOR)
        group.draw(screen)
        window.flip()


if __name__ == "__main__":
    pygame.init()
    pg_window = pygame.Window(TITLE, WIN_SIZE)
    pg_screen = pg_window.get_surface()

    TextSprite.load_resources()

    try:
        main(pg_window, pg_screen)
    finally:
        pygame.quit()
        print("Done.")
