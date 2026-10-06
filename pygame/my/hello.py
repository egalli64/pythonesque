"""
A few simple PyGame apps: https://github.com/egalli64/pythonesque/ pygame/my folder

A Hello PyGame app
"""
import pygame

TITLE = "Hello, pygame-ce!"
WIN_SIZE = (300, 300)
WIN_POS = (50, 50)
FPS = 30  # For such a simple app, 30 frames for second is more than enough
BACKGROUND_COLOR = "darkgray"


def main() -> None:
    window = pygame.Window(TITLE, WIN_SIZE, WIN_POS)
    screen = window.get_surface()
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
        window.flip()


if __name__ == "__main__":
    pygame.init()

    try:
        main()
    finally:
        pygame.quit()
