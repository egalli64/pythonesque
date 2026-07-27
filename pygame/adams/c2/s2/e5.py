"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Particle swarm /4
"""
from random import uniform
from typing import ClassVar

import pygame
from e1 import handle_events
from e4 import random_spread, random_particle_color

FPS = 30
TITLE = "Particle swarm /4"
WIN_SIZE = (300, 600)
WIN_POS = (10, 50)
BACKGROUND_COLOR = "white"
DELTA_SPREAD = 2
X_VELOCITY_RANGE = (-1, 1)
Y_VELOCITY_RANGE = (-10, 0)


class Particle:
    GRAVITY: ClassVar[float] = 0.3
    RADIUS: ClassVar[int] = 2

    def __init__(self, pos: tuple[int, int]) -> None:
        self.pos = pygame.Vector2(pos) + random_spread(DELTA_SPREAD)
        self.color = random_particle_color()
        self.velocity = pygame.Vector2(uniform(*X_VELOCITY_RANGE), uniform(*Y_VELOCITY_RANGE))

    def update(self) -> None:
        self.velocity.y += Particle.GRAVITY
        self.pos += self.velocity

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


if __name__ == "__main__":
    pygame.init()

    try:
        main()
    finally:
        pygame.quit()
