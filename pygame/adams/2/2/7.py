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


class Meadow:
    """Helper class for the stage lower side"""

    COLOR = (50, 180, 50)
    RECT = (0, HORIZON, WIN_SIZE[0], WIN_SIZE[1] - HORIZON)

    def draw(self, screen) -> None:
        pygame.draw.rect(screen, Meadow.COLOR, Meadow.RECT)


class Sky:
    """Helper class for the stage upper side - with dynamic color"""

    COLOR = (100, 150, 255)
    RECT = (0, 0, WIN_SIZE[0], HORIZON)

    def __init__(self) -> None:
        self.color: list[int] = list(Sky.COLOR)

    def update(self, brightness: float) -> None:
        self.color[1] = int(80 + brightness * 120)

    def draw(self, screen) -> None:
        pygame.draw.rect(screen, self.color, Sky.RECT)


class Tree:
    """Helper class for a fixed element"""

    TRUNK_RECT = (100, HORIZON - 50, 20, 60)
    TRUNK_COLOR = (120, 80, 40)
    CROWN_CENTER = (TRUNK_RECT[0] + 10, TRUNK_RECT[1] - 20)
    CROWN_RADIUS = 35
    CROWN_COLOR = (20, 140, 20)

    def draw(self, screen) -> None:
        pygame.draw.rect(screen, Tree.TRUNK_COLOR, Tree.TRUNK_RECT)
        pygame.draw.circle(
            screen, Tree.CROWN_COLOR, Tree.CROWN_CENTER, Tree.CROWN_RADIUS
        )


class House:
    """Helper class for another fixed element"""

    XY = (200, HORIZON - 70)
    BULK_COLOR = (200, 100, 100)
    BULK_RECT = (XY, (150, 100))
    ROOF_COLOR = (150, 50, 50)
    ROOF_POINTS = (XY, (XY[0] + 75, XY[1] - 60), (XY[0] + 150, XY[1]))
    DOOR_COLOR = (100, 60, 30)
    DOOR_XY = (XY[0] + 60, XY[1] + 40)
    DOOR_RECT = ((XY[0] + 60, XY[1] + 40), (30, 60))

    def draw(self, screen) -> None:
        pygame.draw.rect(screen, House.BULK_COLOR, House.BULK_RECT)
        pygame.draw.polygon(screen, House.ROOF_COLOR, self.ROOF_POINTS)
        pygame.draw.rect(screen, House.DOOR_COLOR, House.DOOR_RECT)


class Sun:
    """Helper class for the dynamic element"""

    SPEED = 1
    RADIUS = 40
    COLOR = (255, 220, 0)

    def __init__(self) -> None:
        self.pos = pygame.Vector2(0, 0)

    def update(self) -> float:
        """
        Adjust the Sun position in the sky.

        Return sine-adjusted y position variation in [0, 1].
        """
        if 0 <= self.pos.x < WIN_SIZE[0]:
            self.pos.x += Sun.SPEED
            delta = math.sin((self.pos[0] / WIN_SIZE[0]) * math.pi)
            self.pos.y = HORIZON * (1 - delta) + Sun.RADIUS
            return delta
        else:
            return 0

    def draw(self, screen) -> None:
        if 0 < self.pos.x < WIN_SIZE[0]:
            pygame.draw.circle(screen, Sun.COLOR, self.pos, Sun.RADIUS)


def main():
    pygame.init()
    window = pygame.Window(TITLE, WIN_SIZE)
    screen = window.get_surface()
    clock = pygame.time.Clock()
    meadow = Meadow()
    sky = Sky()
    tree = Tree()
    house = House()
    sun = Sun()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Updates
        delta = sun.update()
        sky.update(delta)

        # Draw
        sky.draw(screen)
        sun.draw(screen)
        meadow.draw(screen)
        tree.draw(screen)
        house.draw(screen)

        window.flip()
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
    print("Done.")
