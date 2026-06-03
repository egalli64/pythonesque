"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Using clock, control frame rate and avoid CPU hogging
"""

import pygame

FPS = 30

TITLE = "Hello, pygame-ce!"
WIN_SIZE = pygame.Vector2(400, 100)
WIN_POS = pygame.Vector2(10, 50)
BACKGROUND_COLOR = (0, 255, 0)


def main():
    pygame.init()
    window = pygame.Window(size=WIN_SIZE, title=TITLE, position=WIN_POS)
    screen = window.get_surface()
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill(BACKGROUND_COLOR)
        window.flip()
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
    print("Done.")
