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
    """Helper class to manage the stage"""

    COLOR = (50, 180, 50)

    def __init__(self) -> None:
        self.rect = (0, HORIZON, WIN_SIZE.x, WIN_SIZE.y - HORIZON)

    def draw(self, screen) -> None:
        pygame.draw.rect(screen, Meadow.COLOR, self.rect)


def main():
    pygame.init()
    window = pygame.Window(TITLE, WIN_SIZE)
    screen = window.get_surface()
    clock = pygame.time.Clock()
    meadow = Meadow()

    running = True
    while running:
        # Watch for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Updates

        # Draw
        meadow.draw(screen)
        window.flip()
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
    print("Done.")
