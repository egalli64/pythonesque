"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Particle swarm /2 - generate static particles, with some ramdomness
"""

from dataclasses import dataclass, field
from random import randint
from typing import ClassVar

import pygame

FPS = 30
TITLE = "Particle swarm /2"
WIN_SIZE = (300, 600)
WIN_POS = (10, 50)
BACKGROUND_COLOR = "white"


def random_color() -> tuple[int, int, int]:
    return randint(0, 255), randint(0, 255), 0


@dataclass(frozen=True)
class Circle:
    DEFAULT_RADIUS: ClassVar[int] = 2

    pos: tuple[int, int]
    color: tuple[int, int, int] | str = field(default_factory=random_color)
    radius: int = DEFAULT_RADIUS

    def __post_init__(self):
        randomized = self.pos[0] + randint(-5, 5), self.pos[1] + randint(-5, 5)
        object.__setattr__(self, "pos", randomized)

    def draw(self, surface: pygame.Surface) -> None:
        pygame.draw.circle(surface, self.color, self.pos, self.radius)


# noinspection DuplicatedCode
def main():
    window = pygame.Window(TITLE, WIN_SIZE, WIN_POS)
    screen = window.get_surface()
    clock = pygame.time.Clock()
    circles = set()

    running = True
    while running:
        clock.tick(FPS)
        running = handle_events()

        if pygame.mouse.get_pressed()[0]:
            circles.add(Circle(pygame.mouse.get_pos()))

        screen.fill(BACKGROUND_COLOR)
        for circle in circles:
            circle.draw(screen)

        window.flip()


# noinspection DuplicatedCode
def handle_events() -> bool:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True


if __name__ == "__main__":
    pygame.init()

    try:
        main()
    finally:
        pygame.quit()
        print("Done.")
