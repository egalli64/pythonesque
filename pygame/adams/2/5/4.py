"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Better encapsulation with a Game class
"""

from enum import Enum, auto
from typing import override
import pygame

WIN_RECT = pygame.Rect(0, 0, 600, 100)


class Defender(pygame.sprite.Sprite):
    IMAGE = "../images/defender.png"
    SIZE = (30, 30)
    DEFAULT_SPEED = 150  # pixel/second
    BOTTOM_GAP = 5

    rect: pygame.FRect
    image: pygame.Surface

    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.image.load(Defender.IMAGE).convert_alpha()
        self.image = pygame.transform.scale(self.image, Defender.SIZE)  # type: ignore
        self.rect = pygame.FRect(self.image.get_rect())  # type: ignore
        self.rect.centerx = WIN_RECT.centerx
        self.rect.bottom = WIN_RECT.bottom - Defender.BOTTOM_GAP
        self.speed = Defender.DEFAULT_SPEED

    def reverse_direction(self) -> None:
        self.speed *= -1

    @override
    def update(self, dt) -> None:
        self.rect.move_ip(self.speed * dt, 0)


class Border(pygame.sprite.Sprite):
    class Position(Enum):
        LEFT = auto()
        RIGHT = auto()

    IMAGE = "../images/brick.png"
    SIZE = (35, WIN_RECT.height)

    def __init__(self, position: Position) -> None:
        super().__init__()
        self.image = pygame.image.load(Border.IMAGE).convert_alpha()
        self.image = pygame.transform.scale(self.image, Border.SIZE)
        self.rect = self.image.get_rect()
        if position == Border.Position.RIGHT:
            self.rect.right = WIN_RECT.right


class Game:
    FPS = 30

    TITLE = "Sprite"
    WIN_POS = (10, 50)
    BACKGROUND_COLOR = "white"

    def __init__(self) -> None:
        self.window = pygame.Window(Game.TITLE, WIN_RECT.size, Game.WIN_POS)
        self.screen = self.window.get_surface()
        self.clock = pygame.time.Clock()

        self.defender = Defender()
        self.borders = pygame.sprite.Group()
        self.borders.add(Border(Border.Position.LEFT))
        self.borders.add(Border(Border.Position.RIGHT))
        self.all_sprites = pygame.sprite.Group(self.defender, self.borders)

    def run(self) -> None:
        """Run the main game loop"""
        while self.handle_events():
            dt = self.clock.tick(Game.FPS) / 1000
            self.update(dt)
            self.draw()

    def handle_events(self) -> bool:
        """Run the event loops, return False in case of termination request"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        return True

    def update(self, dt) -> None:
        if pygame.sprite.spritecollide(self.defender, self.borders, False):
            self.defender.reverse_direction()
        self.defender.update(dt)

    def draw(self) -> None:
        self.screen.fill(Game.BACKGROUND_COLOR)
        self.all_sprites.draw(self.screen)
        self.window.flip()


if __name__ == "__main__":
    pygame.init()

    try:
        Game().run()
    finally:
        pygame.quit()
        print("Done.")
