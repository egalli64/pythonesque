"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Minimal pygame app - classical way
"""

import pygame

SCREEN_SIZE = (400, 100)
TITLE = "Hello, pygame-ce!"
BACKGROUND_COLOR = "white"


def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption(TITLE)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BACKGROUND_COLOR)
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
    print("Done.")
