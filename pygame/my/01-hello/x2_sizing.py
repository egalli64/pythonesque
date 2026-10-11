"""
A few simple PyGame apps: https://github.com/egalli64/pythonesque/ pygame/my folder

Extra 2: Playing with window size
"""
import pygame

TITLE = "Hello, resizable pygame-ce!"
WIN_SIZE = (400, 200)
FPS = 30
BACKGROUND_COLOR = "lightgray"


def main() -> None:
    window = pygame.Window(TITLE, WIN_SIZE, pygame.WINDOWPOS_CENTERED, resizable=True)
    window.minimum_size = (200, 200)
    window.maximum_size = (500, 500)

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
