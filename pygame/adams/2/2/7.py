"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Landscape example
"""

import math
import pygame

FPS = 30

TITLE = "A Peaceful Day"
WIN_SIZE = (600, 400)
HORIZON = 250  # y-level between sky and meadow

MEADOW_COLOR = (50, 180, 50)
MEADOW_RECT = (0, HORIZON, WIN_SIZE[0], WIN_SIZE[1] - HORIZON)

TREE_TRUNK_RECT = (100, HORIZON - 50, 20, 60)
TREE_TRUNK_COLOR = (120, 80, 40)
TREE_CROWN_CENTER = (TREE_TRUNK_RECT[0] + 10, TREE_TRUNK_RECT[1] - 20)
TREE_CROWN_RADIUS = 35
TREE_CROWN_COLOR = (20, 140, 20)


def meadow_draw(surface: pygame.Surface) -> None:
    pygame.draw.rect(surface, MEADOW_COLOR, MEADOW_RECT)


def tree_draw(surface: pygame.Surface) -> None:
    pygame.draw.rect(surface, TREE_TRUNK_COLOR, TREE_TRUNK_RECT)
    pygame.draw.circle(surface, TREE_CROWN_COLOR, TREE_CROWN_CENTER, TREE_CROWN_RADIUS)


class Sky:
    INITIAL_COLOR = (100, 150, 255)
    RECT = (0, 0, WIN_SIZE[0], HORIZON)

    def __init__(self) -> None:
        self.color: list[int] = list(Sky.INITIAL_COLOR)

    def update(self, brightness: float) -> None:
        self.color[1] = int(80 + brightness * 120)

    def draw(self, surface) -> None:
        pygame.draw.rect(surface, self.color, Sky.RECT)


class House:
    """Grouping for the house components"""
    XY = (200, HORIZON - 70)
    BULK_COLOR = (200, 100, 100)
    BULK_RECT = (XY, (150, 100))
    ROOF_COLOR = (150, 50, 50)
    ROOF_POINTS = (XY, (XY[0] + 75, XY[1] - 60), (XY[0] + 150, XY[1]))
    DOOR_COLOR = (100, 60, 30)
    DOOR_RECT = ((XY[0] + 60, XY[1] + 40), (30, 60))

    @staticmethod
    def draw(surface: pygame.Surface) -> None:
        pygame.draw.rect(surface, House.BULK_COLOR, House.BULK_RECT)
        pygame.draw.polygon(surface, House.ROOF_COLOR, House.ROOF_POINTS)
        pygame.draw.rect(surface, House.DOOR_COLOR, House.DOOR_RECT)


class Sun:
    SPEED = 1
    RADIUS = 40
    COLOR = (255, 220, 0)

    def __init__(self) -> None:
        self.pos = pygame.Vector2(0, 0)
        self.brightness = 0.0

    def update(self) -> None:
        if 0 <= self.pos.x < WIN_SIZE[0]:
            self.pos.x += Sun.SPEED
            self.brightness = math.sin((self.pos.x / WIN_SIZE[0]) * math.pi)
            self.pos.y = HORIZON * (1 - self.brightness) + self.RADIUS
        else:
            self.brightness = 0.0

    def draw(self, surface: pygame.Surface) -> None:
        if 0 < self.pos.x < WIN_SIZE[0]:
            pygame.draw.circle(surface, Sun.COLOR, self.pos, Sun.RADIUS)


def main() -> None:
    window = pygame.Window(TITLE, WIN_SIZE)
    screen = window.get_surface()
    clock = pygame.time.Clock()

    sky = Sky()
    sun = Sun()

    running = True
    while running:
        clock.tick(FPS)
        running = handle_events()

        sun.update()
        sky.update(sun.brightness)

        sky.draw(screen)
        sun.draw(screen)
        meadow_draw(screen)
        tree_draw(screen)
        House.draw(screen)
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
