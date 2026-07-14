"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Particle swarm /3
"""

from random import randint, uniform
from typing import ClassVar

import pygame

FPS = 30
TITLE = "Particle swarm /3"
# noinspection DuplicatedCode
WIN_SIZE = (300, 600)
WIN_POS = (10, 50)
BACKGROUND_COLOR = "white"
Y_VELOCITY_RANGE = (-10, 0)


def random_spread() -> tuple[int, int]:
    return randint(-2, 2), randint(-2, 2)


def random_particle_color() -> tuple[int, int, int]:
    return randint(0, 255), randint(0, 255), 0


class Particle:
    GRAVITY: ClassVar[float] = 0.3
    RADIUS: ClassVar[int] = 2

    def __init__(self, pos: tuple[int, int]) -> None:
        self.pos = pygame.Vector2(pos) + random_spread()
        self.color = random_particle_color()
        self.velocity_y = uniform(*Y_VELOCITY_RANGE)

    def update(self) -> None:
        self.velocity_y += Particle.GRAVITY
        self.pos.y += self.velocity_y

    def draw(self, surface: pygame.Surface) -> None:
        pygame.draw.circle(surface, self.color, self.pos, Particle.RADIUS)


# noinspection DuplicatedCode
def main() -> None:
    window = pygame.Window(TITLE, WIN_SIZE, WIN_POS)
    screen = window.get_surface()
    clock = pygame.time.Clock()
    particles: list[Particle] = []

    running = True
    while running:
        clock.tick(FPS)
        running = handle_events()

        if pygame.mouse.get_pressed()[0]:
            particles.append(Particle(pygame.mouse.get_pos()))
        for particle in particles:
            particle.update()

        screen.fill(BACKGROUND_COLOR)
        for particle in particles:
            particle.draw(screen)
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
