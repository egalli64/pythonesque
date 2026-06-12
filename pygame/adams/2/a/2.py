"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Double click - simple but platform dependent
"""

import pygame

FPS = 30

WIN_RECT = pygame.Rect(0, 0, 400, 100)
TITLE = "Double click me"
BACKGROUND_COLOR = "white"


def main():
    window = pygame.Window(TITLE, WIN_RECT.size)
    screen = window.get_surface()
    clock = pygame.time.Clock()

    running = True
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # LEFT
                    if event.clicks == 1:
                        print("Single click")
                    elif event.clicks == 2:
                        print("Double click")

        screen.fill(BACKGROUND_COLOR)
        window.flip()


if __name__ == "__main__":
    pygame.init()

    try:
        main()
    finally:
        pygame.quit()
        print("Done.")
