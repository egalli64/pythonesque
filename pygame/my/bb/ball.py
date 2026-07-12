"""
A few simple PyGame apps: https://github.com/egalli64/pythonesque/ pygame/my folder

Bouncing Ball
"""
import pygame

DEFAULT_RADIUS = 20
DEFAULT_COLOR = "red"
DEFAULT_VELOCITY = (200, -100)


class Ball:
    def __init__(self, pos, radius=DEFAULT_RADIUS, color=DEFAULT_COLOR, velocity=DEFAULT_VELOCITY) -> None:
        self.pos = pygame.Vector2(pos)
        self.velocity = pygame.Vector2(velocity)
        self.radius = radius
        self.color = color

    def update(self, dt: float) -> None:
        self.pos += self.velocity * dt

    def draw(self, surface: pygame.Surface) -> None:
        pygame.draw.circle(surface, self.color, self.pos, self.radius)
