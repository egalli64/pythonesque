"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Multiple windows
"""

import pygame

SCREEN_SIZE = pygame.Vector2(300, 100)
TITLE_1 = "Main Window"
TITLE_2 = "Side Window"
SCREEN_POS_1 = pygame.Vector2(500, 50)
SCREEN_POS_2 = pygame.Vector2(820, 50)
BACKGROUND_COLORS = ((0, 255, 0), (255, 0, 0))
FPS = 30


def main():
    pygame.init()
    windows = {
        pygame.Window(size=SCREEN_SIZE, title=TITLE_1, position=SCREEN_POS_1),
        pygame.Window(size=SCREEN_SIZE, title=TITLE_2, position=SCREEN_POS_2),
    }
    print(windows)

    background_colors = {}
    for window, color in zip(windows, BACKGROUND_COLORS):
        background_colors[window.id] = color

    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Closing last window:", event)
                running = False
            elif event.type == pygame.WINDOWCLOSE:
                print("Close request from window", event.window.id)
                event.window.hide()
                windows.discard(event.window)

        if running:
            for window in windows:
                screen = window.get_surface()
                screen.fill(background_colors[window.id])
                window.flip()
            clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
    print("Done.")
