"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Using locally installed fonts
"""

import pygame

WIN_SIZE = (600, 100)
TITLE = "Local font"
# see https://www.fontsquirrel.com/fonts/list/tag/historical
FONT_NAME = "./font/rothenbg.ttf"
FONT_SIZE = 24

BACKGROUND_COLOR = "white"
TEXT_COLOR = "black"
FPS = 10


def main(window: pygame.Window, screen: pygame.Surface):
    viewport = screen.get_rect()

    font = pygame.font.Font(FONT_NAME, FONT_SIZE)
    text = "This is an example of printing text using a locally installed font"

    screen.fill(BACKGROUND_COLOR)
    # Render and center the text
    text_surface = font.render(text, True, TEXT_COLOR)
    text_rect = text_surface.get_rect(center=viewport.center)
    screen.blit(text_surface, text_rect)
    window.flip()

    running = True
    clock = pygame.time.Clock()
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False


if __name__ == "__main__":
    pygame.init()
    pg_window = pygame.Window(TITLE, WIN_SIZE)
    pg_screen = pg_window.get_surface()

    try:
        main(pg_window, pg_screen)
    finally:
        pygame.quit()
        print("Done.")
