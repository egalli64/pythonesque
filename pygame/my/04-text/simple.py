"""
My PyGame CE tutorial: https://github.com/egalli64/pythonesque/ pygame/my folder

Text rendering: Font, render, blit
"""
import pygame

WIN_SIZE = (700, 100)
TITLE = "Text"
BACKGROUND_COLOR = "whitesmoke"
FPS = 30

TEXT_COLOR = "black"
FONT_SIZE = 32


def main(window: pygame.Window, screen: pygame.Surface) -> None:
    viewport = screen.get_rect()

    font = pygame.font.Font(None, FONT_SIZE)
    text = "Hello, gamer!"
    text_surface = font.render(text, True, TEXT_COLOR)
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
    main_window = pygame.Window(TITLE, WIN_SIZE)
    main_screen = main_window.get_surface()

    try:
        main(main_window, main_screen)
    finally:
        pygame.quit()
