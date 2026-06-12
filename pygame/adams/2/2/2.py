"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Particle swarm /1 - create static particles
"""

from dataclasses import dataclass

import pygame

FPS = 30

TITLE = "Particle swarm /1"
WIN_SIZE = (300, 600)
WIN_POS = (10, 50)
BACKGROUND_COLOR = "white"


@dataclass(frozen=True)
class Circle:
    screen: pygame.Surface
    pos: tuple[int, int]

    RADIUS = 20
    COLOR = "blue"

    def draw(self) -> None:
        pygame.draw.circle(self.screen, Circle.COLOR, self.pos, Circle.RADIUS)


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
