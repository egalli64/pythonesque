"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Text as a Sprite
"""

from typing import Tuple, override
import pygame

FPS = 30

WIN_RECT = pygame.Rect(0, 0, 400, 100)
WIN_POS = (10, 50)
BACKGROUND_COLOR = "cornsilk1"
TITLE = "Text"


class TextSprite(pygame.sprite.Sprite):
    DEFAULT_TEXT = "Hello World!"
    DEFAULT_SIZE = 24
    DEFAULT_COLOR = (0, 0, 255)

    def __init__(self, center: Tuple[int, int], text: str = DEFAULT_TEXT) -> None:
        super().__init__()

        self.image = None
        self.rect = None
        self.size = TextSprite.DEFAULT_SIZE
        self.font = pygame.font.SysFont(None, self.size)
        self.color: list[int] = list(TextSprite.DEFAULT_COLOR)
        self.text = text
        self.center = center
        self.dirty = True
        self.render()

    def render(self) -> None:
        self.image = self.font.render(self.text, True, self.color)
        self.rect = self.image.get_rect()
        self.rect.center = self.center
        self.dirty = False
        print(self.size, self.color)

    def change_text(self, text: str) -> None:
        self.text = text
        self.dirty = True

    def change_size(self, step: int = 1) -> None:
        self.size += step
        self.font = pygame.font.SysFont(None, self.size)
        self.dirty = True

    def change_color(self, delta: Tuple[int, int, int]) -> None:
        for i in range(3):
            self.color[i] = (self.color[i] + delta[i]) % 256
        self.dirty = True

    @override
    def update(self) -> None:
        if self.dirty:
            self.render()


def main():
    pygame.init()

    window = pygame.Window(TITLE, WIN_RECT.size, WIN_POS)
    screen = window.get_surface()
    clock = pygame.time.Clock()

    hello = TextSprite(WIN_RECT.center)
    text_group = pygame.sprite.Group(hello)

    running = True
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                # change font size
                elif event.key == pygame.K_KP_PLUS or event.key == pygame.K_PLUS:
                    hello.change_size(+1)
                elif event.key == pygame.K_KP_MINUS or event.key == pygame.K_MINUS:
                    hello.change_size(-1)
                # change font color - red channel
                elif event.key == pygame.K_r:
                    if event.mod & pygame.KMOD_SHIFT:
                        hello.change_color((-1, 0, 0))
                    else:
                        hello.change_color((+1, 0, 0))
                # change font color - green channel
                elif event.key == pygame.K_g:
                    if event.mod & pygame.KMOD_SHIFT:
                        hello.change_color((0, -1, 0))
                    else:
                        hello.change_color((0, +1, 0))
                # change font color - blue channel
                elif event.key == pygame.K_b:
                    if event.mod & pygame.KMOD_SHIFT:
                        hello.change_color((0, 0, -1))
                    else:
                        hello.change_color((0, 0, +1))

        text_group.update()

        screen.fill(BACKGROUND_COLOR)
        text_group.draw(screen)
        window.flip()


if __name__ == "__main__":
    main()
    pygame.quit()
