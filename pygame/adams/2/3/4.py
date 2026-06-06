"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Landscape blit - !!! Caching surfaces is not useful in such simple cases !!!
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
    POS = (0, HORIZON)
    SIZE = (WIN_SIZE[0], WIN_SIZE[1] - HORIZON)

    def __init__(self) -> None:
        """!!! Not caching is probably cheaper !!!"""
        self.surface = pygame.Surface(Meadow.SIZE).convert()
        self.surface.fill(Meadow.COLOR)

    def draw(self, screen) -> None:
        screen.blit(self.surface, Meadow.POS)


class Sky:
    """Helper class for the stage upper side - with dynamic color"""

    COLOR = (100, 150, 255)
    POS = (0, 0)
    SIZE = (WIN_SIZE[0], HORIZON)

    def __init__(self) -> None:
        """!!! Drawing the rectangle instead is probably cheaper !!!"""
        self.surface = pygame.Surface(Sky.SIZE).convert()

    def update(self, brightness: float) -> None:
        color = Sky.COLOR[0], int(80 + brightness * 120), Sky.COLOR[2]
        self.surface.fill(color)

    def draw(self, screen) -> None:
        screen.blit(self.surface, Sky.POS)


class Tree:
    """Helper class for a fixed element"""

    POS = (65, HORIZON - 100)
    SIZE = (90, 120)
    TRUNK_RECT = (35, 60, 20, 60)
    TRUNK_COLOR = (120, 80, 40)
    CROWN_CENTER = (TRUNK_RECT[0] + 10, TRUNK_RECT[1] - 20)
    CROWN_RADIUS = 35
    CROWN_COLOR = (20, 140, 20)

    def __init__(self) -> None:
        """!!! Not caching is probably cheaper !!!"""
        self.surface = pygame.Surface(Tree.SIZE, pygame.SRCALPHA).convert_alpha()
        pygame.draw.rect(self.surface, Tree.TRUNK_COLOR, Tree.TRUNK_RECT)
        pygame.draw.circle(
            self.surface, Tree.CROWN_COLOR, Tree.CROWN_CENTER, Tree.CROWN_RADIUS
        )

    def draw(self, screen) -> None:
        screen.blit(self.surface, Tree.POS)


class House:
    """Helper class for another fixed element"""

    POS = (200, HORIZON - 120)
    SIZE = (150, 160)
    BULK_COLOR = (200, 100, 100)
    BULK_RECT = (0, 60, 150, 100)
    ROOF_COLOR = (150, 50, 50)
    ROOF_POINTS = ((0, 60), (75, 0), (150, 60))
    DOOR_COLOR = (100, 60, 30)
    DOOR_RECT = (60, 100, 30, 60)

    def __init__(self) -> None:
        """!!! Not caching is probably cheaper !!!"""
        self.surface = pygame.Surface(House.SIZE, pygame.SRCALPHA).convert_alpha()
        pygame.draw.rect(self.surface, House.BULK_COLOR, House.BULK_RECT)
        pygame.draw.polygon(self.surface, House.ROOF_COLOR, House.ROOF_POINTS)
        pygame.draw.rect(self.surface, House.DOOR_COLOR, self.DOOR_RECT)

    def draw(self, screen) -> None:
        screen.blit(self.surface, House.POS)


class Sun:
    """Helper class for the dynamic element"""

    SPEED = 1
    RADIUS = 40
    CENTER = (RADIUS, RADIUS)
    SIZE = (RADIUS * 2, RADIUS * 2)
    COLOR = (255, 220, 0)

    def __init__(self) -> None:
        """!!! Not caching is probably cheaper !!!"""
        self.pos = pygame.Vector2(0, 0)
        self.surface = pygame.Surface(Sun.SIZE, pygame.SRCALPHA).convert_alpha()
        pygame.draw.circle(self.surface, Sun.COLOR, Sun.CENTER, Sun.RADIUS)

    def update(self) -> float:
        """
        Adjust the Sun position in the sky.

        Return sine-adjusted y position variation in [0, 1].
        """
        if 0 <= self.pos.x < WIN_SIZE[0]:
            self.pos[0] += Sun.SPEED
            delta = math.sin((self.pos[0] / WIN_SIZE[0]) * math.pi)
            self.pos.y = round(HORIZON * (1 - delta))
            return delta
        else:
            return 0

    def draw(self, screen) -> None:
        if 0 < self.pos.x < WIN_SIZE[0]:
            screen.blit(self.surface, (self.pos[0], self.pos[1]))


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
