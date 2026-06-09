"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Another minimal pygame app - modern way, explicit Window
"""

import pygame

WIN_SIZE = (400, 100)
WIN_POS = (10, 50)
TITLE = "Hello, pygame-ce!"
BACKGROUND_COLOR = (0, 255, 0)


def main():
    window = pygame.Window(title=TITLE, size=WIN_SIZE, position=WIN_POS)
    screen = window.get_surface()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BACKGROUND_COLOR)
        window.flip()


if __name__ == "__main__":
    pygame.init()

    try:
        main()
    finally:
        pygame.quit()
        print("Done.")
