"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Sprite collision
"""

from enum import Enum, auto

import pygame

FPS = 30

TITLE = "Sprite"
WIN_RECT = pygame.Rect(0, 0, 600, 100)
WIN_POS = (10, 50)
BACKGROUND_COLOR = "white"


class Position(Enum):
    LEFT = auto()
    RIGHT = auto()


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

    def update(self, dt) -> None:
        self.rect.move_ip(self.speed * dt, 0)

    def draw(self, screen: pygame.Surface) -> None:
        screen.blit(self.image, self.rect)

    def change_direction(self) -> None:
        self.speed *= -1


class Border(pygame.sprite.Sprite):
    IMAGE = "../images/brick.png"
    SIZE = (35, WIN_RECT.height)

    rect: pygame.Rect
    image: pygame.Surface

    def __init__(self, position: Position) -> None:
        super().__init__()
        self.image = pygame.image.load(Border.IMAGE).convert_alpha()
        self.image = pygame.transform.scale(self.image, Border.SIZE)  # type: ignore
        self.rect = self.image.get_rect()  # type: ignore
        if position == Position.RIGHT:
            self.rect.left = WIN_RECT.width - self.rect.width

    def draw(self, screen: pygame.Surface) -> None:
        screen.blit(self.image, self.rect)


def main():
    pygame.init()

    window = pygame.Window(TITLE, WIN_RECT.size, WIN_POS)
    screen = window.get_surface()
    clock = pygame.time.Clock()

    defender = Defender()
    border_left = Border(Position.LEFT)
    border_right = Border(Position.RIGHT)

    running = True
    while running:
        dt = clock.tick(FPS) / 1000

        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update
        if pygame.sprite.collide_rect(defender, border_left):
            defender.change_direction()
        elif pygame.sprite.collide_rect(defender, border_right):
            defender.change_direction()
        defender.update(dt)

        # Draw
        screen.fill((255, 255, 255))
        defender.draw(screen)
        border_left.draw(screen)
        border_right.draw(screen)

        window.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
    print("Done.")
