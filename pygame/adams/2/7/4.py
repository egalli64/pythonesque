"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Using locally installed fonts
"""

import pygame

WIN_RECT = pygame.Rect(0, 0, 600, 100)
TITLE = "Local font"
# see https://www.fontsquirrel.com/fonts/list/tag/historical
FONT_NAME = "./font/rothenbg.ttf"
FONT_SIZE = 24

BACKGROUND_COLOR = "white"
TEXT_COLOR = "black"

FPS = 30


def main():
    window = pygame.Window(TITLE, WIN_RECT.size)

    screen = window.get_surface()
    clock = pygame.time.Clock()
    all_sprites = pygame.sprite.Group()

    font = pygame.font.Font(FONT_NAME, FONT_SIZE)
    text = "This is an example of printing text using a locally installed font"

    running = True
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        all_sprites.update()
        screen.fill(BACKGROUND_COLOR)
        # Render and center the text
        text_surface = font.render(text, True, TEXT_COLOR)
        text_rect = text_surface.get_rect(center=(WIN_RECT.center))
        screen.blit(text_surface, text_rect)
        all_sprites.draw(screen)
        window.flip()


if __name__ == "__main__":
    pygame.init()

    try:
        main()
    finally:
        pygame.quit()
        print("Done.")
