"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Double click - simple but platform dependent
"""
import pygame

FPS = 30
WIN_SIZE = (400, 100)
TITLE = "Double click me"
BACKGROUND_COLOR = "white"


def main(window: pygame.Window, screen: pygame.Surface) -> None:
    clock = pygame.time.Clock()

    running = True
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    running = False
                case pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                case pygame.MOUSEBUTTONDOWN:
                    if event.button == pygame.BUTTON_LEFT:
                        if event.clicks == 1:
                            print("Single click")
                        elif event.clicks >= 2:
                            print(f"Double click (or more: {event.clicks} clicks detected)")

        screen.fill(BACKGROUND_COLOR)
        window.flip()


if __name__ == "__main__":
    pygame.init()
    pg_window = pygame.Window(TITLE, WIN_SIZE)
    pg_screen = pg_window.get_surface()

    try:
        main(pg_window, pg_screen)
    finally:
        pygame.quit()
        print("Done.")
