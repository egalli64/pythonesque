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
    COLOR = (50, 180, 50)
    POS = (0, HORIZON)
    SIZE = (WIN_SIZE[0], WIN_SIZE[1] - HORIZON)

    def __init__(self) -> None:
        """!!! Not caching is probably cheaper !!!"""
        self.image = pygame.Surface(Meadow.SIZE).convert()
        self.image.fill(Meadow.COLOR)

    def draw(self, surface: pygame.Surface) -> None:
        surface.blit(self.image, Meadow.POS)


class Sky:
    INITIAL_COLOR = (100, 150, 255)
    POS = (0, 0)
    SIZE = (WIN_SIZE[0], HORIZON)

    def __init__(self) -> None:
        """!!! Drawing the rectangle instead is probably cheaper !!!"""
        self.image = pygame.Surface(Sky.SIZE).convert()

    def update(self, brightness: float) -> None:
        color = Sky.INITIAL_COLOR[0], int(80 + brightness * 120), Sky.INITIAL_COLOR[2]
        self.image.fill(color)

    def draw(self, surface: pygame.Surface) -> None:
        surface.blit(self.image, Sky.POS)


class Tree:
    POS = (65, HORIZON - 100)
    SIZE = (90, 120)
    TRUNK_RECT = (35, 60, 20, 60)
    TRUNK_COLOR = (120, 80, 40)
    CROWN_CENTER = (TRUNK_RECT[0] + 10, TRUNK_RECT[1] - 20)
    CROWN_RADIUS = 35
    CROWN_COLOR = (20, 140, 20)

    def __init__(self) -> None:
        """!!! Not caching is probably cheaper !!!"""
        self.image = pygame.Surface(Tree.SIZE, pygame.SRCALPHA).convert_alpha()
        pygame.draw.rect(self.image, Tree.TRUNK_COLOR, Tree.TRUNK_RECT)
        pygame.draw.circle(self.image, Tree.CROWN_COLOR, Tree.CROWN_CENTER, Tree.CROWN_RADIUS)

    def draw(self, surface: pygame.Surface) -> None:
        surface.blit(self.image, Tree.POS)


class House:
    """Grouping for the house components"""
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
        self.image = pygame.Surface(House.SIZE, pygame.SRCALPHA).convert_alpha()
        pygame.draw.rect(self.image, House.BULK_COLOR, House.BULK_RECT)
        pygame.draw.polygon(self.image, House.ROOF_COLOR, House.ROOF_POINTS)
        pygame.draw.rect(self.image, House.DOOR_COLOR, House.DOOR_RECT)

    def draw(self, surface: pygame.Surface) -> None:
        surface.blit(self.image, House.POS)


class Sun:
    SPEED = 1
    RADIUS = 40
    CENTER = (RADIUS, RADIUS)
    SIZE = (RADIUS * 2, RADIUS * 2)
    COLOR = (255, 220, 0)

    def __init__(self) -> None:
        """!!! Not caching is probably cheaper !!!"""
        self.pos = pygame.Vector2(0, 0)
        self.brightness = 0.0
        self.image = pygame.Surface(Sun.SIZE, pygame.SRCALPHA).convert_alpha()
        pygame.draw.circle(self.image, Sun.COLOR, Sun.CENTER, Sun.RADIUS)

    def update(self) -> None:
        if 0 <= self.pos.x < WIN_SIZE[0]:
            self.pos[0] += Sun.SPEED
            self.brightness = math.sin((self.pos.x / WIN_SIZE[0]) * math.pi)
            self.pos.y = round(HORIZON * (1 - self.brightness))
        else:
            self.brightness = 0.0

    def draw(self, surface: pygame.Surface) -> None:
        if 0 < self.pos.x < WIN_SIZE[0]:
            surface.blit(self.image, (self.pos[0], self.pos[1]))


def main():
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
        clock.tick(FPS)
        running = handle_events()

        # Updates
        sun.update()
        sky.update(sun.brightness)

        # Draw
        sky.draw(screen)
        sun.draw(screen)
        meadow.draw(screen)
        tree.draw(screen)
        house.draw(screen)
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
