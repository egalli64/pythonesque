"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Landscape example
"""

import pygame

FPS = 30

TITLE = "Landscape"
WIN_SIZE = pygame.Vector2(600, 400)


def main():
    pygame.init()
    window = pygame.Window(TITLE, WIN_SIZE)
    screen = window.get_surface()

    clock = pygame.time.Clock()

    running = True
    while running:
        # Watch for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Updates

        # Draw
        window.flip()
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
