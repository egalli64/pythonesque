"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Particle swarm /2 - generate static particles, with some ramdomness
"""

from dataclasses import dataclass, field
from random import randint

import pygame

FPS = 30
TITLE = "Particle swarm /2"
WIN_SIZE = (300, 600)
WIN_POS = (10, 50)
BACKGROUND_COLOR = "white"


@dataclass(frozen=True)
class Circle:
    screen: pygame.Surface
    pos: tuple[int, int]
    color: tuple[int, int, int] = field(
        default_factory=lambda: (randint(100, 255), randint(50, 255), 0)
    )

    RADIUS = 2

    def __post_init__(self):
        randomized = self.pos[0] + randint(-5, 5), self.pos[1] + randint(-5, 5)
        object.__setattr__(self, "pos", randomized)

    def draw(self) -> None:
        pygame.draw.circle(self.screen, self.color, self.pos, Circle.RADIUS)


def main():
    window = pygame.Window(TITLE, WIN_SIZE, WIN_POS)
    screen = window.get_surface()
    clock = pygame.time.Clock()
    circles = set()

    while handle_events():
        clock.tick(FPS)

        if pygame.mouse.get_pressed()[0]:
            circles.add(Circle(screen, pygame.mouse.get_pos()))

        screen.fill(BACKGROUND_COLOR)
        for circle in circles:
            circle.draw()

        window.flip()


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
