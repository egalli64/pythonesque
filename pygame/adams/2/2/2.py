"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Particle swarm /1 - create static particles
"""
from dataclasses import dataclass
from typing import ClassVar

import pygame

FPS = 60

TITLE = "Particle swarm /1"
WIN_SIZE = (300, 600)
WIN_POS = (10, 50)
BACKGROUND_COLOR = "darkgray"


@dataclass(frozen=True)
class Circle:
    DEFAULT_COLOR = "blue"
    DEFAULT_RADIUS: ClassVar[int] = 20

    pos: tuple[int, int]
    color: tuple[int, int, int] | str = DEFAULT_COLOR
    radius: int = DEFAULT_RADIUS

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
