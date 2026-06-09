"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Minimal pygame app - in the classic way
"""

import pygame

SCREEN_SIZE = (400, 100)
TITLE = "Hello, pygame-ce!"
BACKGROUND_COLOR = "white"


def main():
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption(TITLE)

    running = True
    # main loop
    while running:
        # event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # update state

        # rendering
        screen.fill(BACKGROUND_COLOR)
        pygame.display.flip()


if __name__ == "__main__":
    pygame.init()

    try:
        main()
    finally:
        pygame.quit()
        print("Done.")
