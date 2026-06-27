"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Simple text rendering
"""

import pygame

FPS = 30

WIN_RECT = pygame.Rect(0, 0, 700, 100)
TITLE = "Text"
BACKGROUND_COLOR = "white"
TEXT_COLOR = "black"


def main():
    window = pygame.Window(TITLE, WIN_RECT.size)
    screen = window.get_surface()
    clock = pygame.time.Clock()

    font = pygame.font.SysFont(None, 24)
    text = "Hello, gamer!"

    while handle_events():
        clock.tick(FPS)

        # update
        screen.fill(BACKGROUND_COLOR)
        surface = font.render(text, True, TEXT_COLOR)
        rect = surface.get_rect(center=(WIN_RECT.width / 2, WIN_RECT.height / 2))

        # draw
        screen.blit(surface, rect)
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

    try:
        main()
    finally:
        pygame.quit()
        print("Done.")
