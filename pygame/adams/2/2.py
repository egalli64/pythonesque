"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Another minimal pygame app - modern way, explicit Window
"""

import pygame

SCREEN_SIZE = pygame.Vector2(400, 100)
TITLE = "Hello, pygame-ce!"
SCREEN_POS = pygame.Vector2(10, 50)
BACKGROUND_COLOR = (0, 255, 0)
FPS = 30


def main():
    pygame.init()
    window = pygame.Window(size=SCREEN_SIZE, title=TITLE, position=SCREEN_POS)
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
