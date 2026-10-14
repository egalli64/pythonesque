"""
My PyGame CE tutorial: https://github.com/egalli64/pythonesque/ pygame/my folder

Extra 3: Borderless window
"""
import pygame

TITLE = "A borderless window"
WIN_SIZE = (400, 100)
WIN_POS = (50, 200)
FPS = 30
BACKGROUND_COLOR = "yellow"


def main() -> None:
    window = pygame.Window(TITLE, WIN_SIZE, WIN_POS, borderless=True)
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
