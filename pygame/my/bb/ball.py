"""
A few simple PyGame apps: https://github.com/egalli64/pythonesque/ pygame/my folder

Bouncing Ball
"""
import random

import pygame

DEFAULT_RADIUS = 20
DEFAULT_COLOR = "red"
COLOR_INTERVAL = (64, 255)
DEFAULT_VELOCITY = (200, -100)
DELTA_SPEED = 0.1


class Ball:
    def __init__(self, center: tuple[int, int], radius: int = DEFAULT_RADIUS, color: str = DEFAULT_COLOR,
                 velocity: tuple[int, int] = DEFAULT_VELOCITY) -> None:
        self.center = pygame.Vector2(center)
        self.radius = radius
        self.color = color
        self.velocity = pygame.Vector2(velocity)

    def bounce_in(self, viewport: pygame.Rect) -> None:
        if self.center.x >= viewport.right - self.radius:
            self.center.x = viewport.right - self.radius
            self.velocity.x *= -1
        elif self.center.x <= viewport.left + self.radius:
            self.center.x = viewport.left + self.radius
            self.velocity.x *= -1

        if self.center.y <= viewport.top + self.radius:
            self.center.y = viewport.top + self.radius
            self.velocity.y *= -1
        elif self.center.y >= viewport.bottom - self.radius:
            self.center.y = viewport.bottom - self.radius
            self.velocity.y *= -1

    def update(self, dt: float, viewport: pygame.Rect) -> None:
        self.center += self.velocity * dt
        self.bounce_in(viewport)

    def draw(self, surface: pygame.Surface) -> None:
        pygame.draw.circle(surface, self.color, self.center, self.radius)

    def change_color(self) -> None:
        self.color = tuple(random.randint(*COLOR_INTERVAL) for _ in range(3))

    def increase_speed(self, delta: float = DELTA_SPEED) -> None:
        self.velocity *= 1 + delta

    def decrease_speed(self, delta: float = DELTA_SPEED) -> None:
        self.velocity *= 1 - delta
