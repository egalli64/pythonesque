"""
A few simple PyGame apps: https://github.com/egalli64/pythonesque/ pygame/my folder

A Hello PyGame app
"""
import pygame

TITLE = "Hello, pygame-ce!"
WIN_SIZE = (300, 300)
WIN_POS = (50, 50)
# For such a simple app, 30 frames for second is more than enough
FPS = 30
BACKGROUND_COLOR = "darkgray"


def main():
    window = pygame.Window(TITLE, WIN_SIZE, WIN_POS)
    screen = window.get_surface()
    clock = pygame.time.Clock()

    running = True
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        screen.fill(BACKGROUND_COLOR)
        window.flip()


if __name__ == "__main__":
    pygame.init()

    try:
        main()
    finally:
        pygame.quit()
