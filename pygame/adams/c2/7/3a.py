"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

List of the first few installed fonts
"""
import pygame

WIN_SIZE = (900, 800)
WIN_POS = (10, 50)
FONT_SIZE = 20
BORDER = 10
TITLE = "List of some installed fonts"
FPS = 10  # the content does not change, no need of high FPS


def main(window: pygame.Window, screen: pygame.Surface):
    viewport = screen.get_rect()
    font_names = pygame.font.get_fonts()
    print(f"There are {len(font_names)} available fonts")

    screen.fill("white")

    y = BORDER
    for name in sorted(font_names):
        # load a font installed on the operating system
        font = pygame.font.SysFont(name, FONT_SIZE)
        text = f"{name}: {font.name} {font.style_name}"
        surface = font.render(text, True, "black")
        rect = surface.get_rect()
        rect.topleft = (BORDER, y)
        pygame.draw.rect(screen, "red", rect, width=1, border_radius=3)
        screen.blit(surface, rect)

        if rect.bottom + BORDER > viewport.bottom:
            break
        else:
            y += surface.get_height()

    window.flip()

    clock = pygame.time.Clock()
    running = True
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
