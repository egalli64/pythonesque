"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Simple text rendering
"""
import pygame

FPS = 30
WIN_SIZE = (700, 100)
TITLE = "Text"
BACKGROUND_COLOR = "white"
TEXT_COLOR = "black"


def main(window: pygame.Window, screen: pygame.Surface) -> None:
    viewport = screen.get_rect()

    font = pygame.font.Font(None, 32)
    text = "Hello, gamer!"
    text_surface = font.render(text, True, TEXT_COLOR)  # antialiasing is usually preferred
    text_rect = text_surface.get_rect(center=viewport.center)

    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(FPS)

        running = handle_events()

        screen.fill(BACKGROUND_COLOR)
        screen.blit(text_surface, text_rect)
        window.flip()


def handle_events() -> bool:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            return False
    return True


if __name__ == "__main__":
    pygame.init()
    pg_window = pygame.Window(TITLE, WIN_SIZE)
    pg_screen = pg_window.get_surface()

    try:
        main(pg_window, pg_screen)
    finally:
        pygame.quit()
        print("Done.")
