"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Particle swarm /6
"""

from random import randint, uniform
from typing import ClassVar

import pygame

FPS = 30
TITLE = "Particle swarm /6"
WIN_SIZE = (300, 600)
WIN_POS = (10, 50)
BACKGROUND_COLOR = "white"


def random_spread() -> tuple[int, int]:
    return randint(-4, 4), randint(-4, 4)


def random_particle_color() -> tuple[int, int, int]:
    return randint(0, 255), randint(0, 255), 0


class Particle:
    GRAVITY: ClassVar[float] = 0.3
    INITIAL_RADIUS: ClassVar[float] = 7.0
    RADIUS_DELTA: ClassVar[float] = 1 / 15

    def __init__(self, pos: tuple[int, int]) -> None:
        self.pos = pygame.Vector2(pos) + random_spread()
        self.color = [randint(100, 255), randint(50, 255), 0]
        self.speed = pygame.Vector2(uniform(-1.5, 1.5), uniform(-10.0, 0.0))
        self.radius = Particle.INITIAL_RADIUS

    def update(self) -> None:
        """Change the particle vertical speed, position, and radius"""
        self.speed.y += Particle.GRAVITY
        self.pos += self.speed
        self.radius -= Particle.RADIUS_DELTA

    def is_lost(self) -> bool:
        """
        Check if the current particle is escaped from the window (left, right, or down), or it is too small to be seen
        """
        return (self.pos.x + self.radius < 0 or self.pos.x - self.radius > WIN_SIZE[0]
                or self.pos.y - self.radius > WIN_SIZE[1] or self.radius < 1)

    def draw(self, surface: pygame.Surface) -> None:
        pygame.draw.circle(surface, self.color, self.pos, self.radius)


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
            for _ in range(5):
                particles.append(Particle(pygame.mouse.get_pos()))

        for particle in particles:
            particle.update()
        particles = [particle for particle in particles if not particle.is_lost()]

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
