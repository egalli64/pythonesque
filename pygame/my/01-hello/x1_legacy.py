"""
My PyGame CE tutorial: https://github.com/egalli64/pythonesque/ pygame/my folder

Extra 1: Legacy main window management by pygame.display functions
"""
import pygame

TITLE = "Hello, legacy pygame-ce!"
WIN_SIZE = (400, 300)
WIN_POS = (100, 200)
FPS = 30
BACKGROUND_COLOR = (100, 100, 100)  # using RGB notation


def main() -> None:
    # legacy approach: nowadays pygame.window.Window is used instead of pygame.display
    screen = pygame.display.set_mode(WIN_SIZE)
    pygame.display.set_caption(TITLE)
    pygame.display.set_window_position(WIN_POS)

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

        screen.fill(BACKGROUND_COLOR)
        pygame.display.flip()  # legacy approach: use window.flip() instead


if __name__ == "__main__":
    pygame.init()

    try:
        main()
    finally:
        pygame.quit()
