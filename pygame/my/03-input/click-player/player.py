"""
My PyGame CE tutorial: https://github.com/egalli64/pythonesque/ pygame/my folder

User input: Mouse events
"""
import pygame

INITIAL_POS = (200.0, 150.0)
RADIUS = 20
SPEED = 4.0

BORDER_COLOR = "black"
INTERNAL_COLORS = ["dodgerblue", "lightblue", "peachpuff", "thistle"]


class Player:
    def __init__(self, pos: tuple[float, float] = INITIAL_POS, radius: float = RADIUS, speed: float = SPEED) -> None:
        self.pos = pygame.Vector2(pos)
        self.radius = radius
        self.speed = speed

        self.color_index = 0
        self.target: pygame.Vector2 | None = None

    def move_to(self, pos: tuple[int, int], viewport: pygame.Rect) -> None:
        # clamp the target position to the reachable internal area
        x = max(self.radius, min(pos[0], viewport.width - self.radius))
        y = max(self.radius, min(pos[1], viewport.height - self.radius))
        self.target = pygame.Vector2(x, y)

    def change_color(self) -> None:
        self.color_index = (self.color_index + 1) % len(INTERNAL_COLORS)

    def change_radius(self, delta: int) -> None:
        self.radius = max(10, min(50, self.radius + (delta * 2)))

    def update(self, viewport: pygame.Rect) -> None:
        if self.target is not None:
            offset = self.target - self.pos

            if offset.length() <= self.speed:
                # close enough, snap to position and stop moving
                self.pos = pygame.Vector2(self.target)
                self.target = None
            else:
                # step towards the target
                offset.normalize_ip()
                self.pos += offset * self.speed

        self.pos.x = max(self.radius, min(self.pos.x, viewport.width - self.radius))
        self.pos.y = max(self.radius, min(self.pos.y, viewport.height - self.radius))

    def draw(self, surface: pygame.Surface) -> None:
        pygame.draw.circle(surface, INTERNAL_COLORS[self.color_index], self.pos, self.radius)
        pygame.draw.circle(surface, BORDER_COLOR, self.pos, self.radius, width=1)
