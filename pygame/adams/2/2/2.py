"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Particle swarm /1
"""

from dataclasses import dataclass

import pygame

FPS = 30

TITLE = "Particle swarm /1"
WIN_SIZE = pygame.Vector2(300, 600)
WIN_POS = pygame.Vector2(10, 50)
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
    pygame.init()
    window = pygame.Window(TITLE, WIN_SIZE, WIN_POS)
    screen = window.get_surface()
    clock = pygame.time.Clock()
    circles = set()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if pygame.mouse.get_pressed()[0]:
            circles.add(Circle(screen, pygame.mouse.get_pos()))
            print("Circles:", circles)

        screen.fill(BACKGROUND_COLOR)
        for circle in circles:
            circle.draw()

        window.flip()
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
    print("Done.")
