"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Landscape example
"""

import pygame

FPS = 30

TITLE = "A Peaceful Day"
WIN_SIZE = pygame.Vector2(600, 400)
HORIZON = 250  # y-level between sky and meadow


class Meadow:
    """Helper class for the stage lower side"""

    COLOR = (50, 180, 50)
    RECT = (0, HORIZON, WIN_SIZE.x, WIN_SIZE.y - HORIZON)

    def draw(self, screen) -> None:
        pygame.draw.rect(screen, Meadow.COLOR, Meadow.RECT)


class Sky:
    """Helper class for the stage upper side"""

    COLOR = (100, 150, 255)
    RECT = (0, 0, WIN_SIZE.x, HORIZON)

    def draw(self, screen) -> None:
        pygame.draw.rect(screen, Sky.COLOR, Sky.RECT)


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


def main():
    pygame.init()
    window = pygame.Window(TITLE, WIN_SIZE)
    screen = window.get_surface()
    clock = pygame.time.Clock()
    meadow = Meadow()
    sky = Sky()
    tree = Tree()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Updates

        # Draw
        meadow.draw(screen)
        sky.draw(screen)
        tree.draw(screen)

        window.flip()
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
    print("Done.")
