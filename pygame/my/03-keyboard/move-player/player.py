"""
My PyGame CE tutorial: https://github.com/egalli64/pythonesque/ pygame/my folder

Objectified Continuous Polling
"""
import pygame

INITIAL_POS = (200.0, 150.0)
RADIUS = 20
SPEED = 4.0

INTERNAL_COLOR = "dodgerblue"
BORDER_COLOR = "darkblue"


class Player:
    def __init__(self, pos: tuple[float, float] = INITIAL_POS, radius: float = RADIUS, speed: float = SPEED) -> None:
        self.pos = pygame.Vector2(pos)
        self.radius = radius
        self.speed = speed
        self.direction = pygame.Vector2(0, 0)

    def set_direction(self, keys: pygame.key.ScancodeWrapper) -> None:
        self.direction.update(0, 0)

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.direction.x -= 1
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.direction.x += 1
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.direction.y -= 1
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.direction.y += 1

    def update(self, viewport: pygame.Rect) -> None:
        if self.direction:
            self.direction.normalize_ip()
            self.pos += self.direction * self.speed

        self.pos.x = max(self.radius, min(self.pos.x, viewport.width - self.radius))
        self.pos.y = max(self.radius, min(self.pos.y, viewport.height - self.radius))

    def draw(self, surface: pygame.Surface) -> None:
        pygame.draw.circle(surface, INTERNAL_COLOR, self.pos, self.radius)
        pygame.draw.circle(surface, BORDER_COLOR, self.pos, self.radius, width=1)
