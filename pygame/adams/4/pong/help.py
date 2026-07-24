"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Pong help
"""
import pygame

TEXT_L = """h
p
ESC

F2
N/A
1
2

UP
DOWN
w
s"""

TEXT_R = """- toggle help mode
- toggle pause mode
- quit

- toggle sound mode
- toggle both paddles AI mode
- toggle left paddle AI mode
- toggle right paddle AI mode

- move right paddle up
- move right paddle down
- move left paddle up
- move left paddle down"""


class Help:
    FONT_COLOR = "white"
    FONT_SIZE = 28

    def __init__(self, viewport: pygame.Rect, *groups) -> None:
        super().__init__(*groups)
        self.rect = pygame.Rect(viewport.topleft, viewport.size)
        self.image = pygame.Surface(self.rect.size).convert_alpha()
        self.image.fill([20, 20, 20, 200])
        font = pygame.font.Font(None, Help.FONT_SIZE)
        lines = font.render(TEXT_L, True, Help.FONT_COLOR)
        self.image.blit(lines, (10, 10))
        lines = font.render(TEXT_R, True, Help.FONT_COLOR)
        self.image.blit(lines, (10 + 70, 10))

    def draw(self, screen):
        screen.blit(self.image, self.rect)
