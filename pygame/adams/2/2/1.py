"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Introduction to graphic primitives
"""

import pygame
import pygame.gfxdraw

FPS = 30
TITLE = "Graphic Primitives"
WIN_SIZE = (530, 530)
WIN_POS = (10, 50)
BACKGROUND_COLOR = pygame.Color(200, 200, 200)


def main():
    window = pygame.Window(TITLE, WIN_SIZE, WIN_POS)
    screen = window.get_surface()
    clock = pygame.time.Clock()

    running = True
    while running:
        clock.tick(FPS)
        running = handle_events()

        screen.fill(BACKGROUND_COLOR)

        draw_filled_rectangle(screen)
        draw_rectangle(screen)

        draw_filled_polygon(screen)
        draw_polygon(screen)

        pygame.draw.line(screen, "red", start_pos=(5, 120), end_pos=(240, 120), width=3)

        pygame.draw.circle(screen, "blue", center=(40, 200), radius=30)
        pygame.draw.circle(screen, "blue", (110, 200), 30, width=3)
        pygame.draw.circle(screen, "blue", (180, 200), 30, 5, draw_top_right=True)

        draw_pixel_classic(screen)
        draw_pixel_rect(screen)
        draw_pixel_modern(screen)
        # for many pixels see surfarray (NumPy based)

        window.flip()


def draw_filled_rectangle(screen: pygame.Surface):
    # read the rectangle as (left, top), (width, height)
    rect = pygame.Rect(10, 10, 20, 30)
    # draw.rect() requires at least a screen, a color, and a rect
    pygame.draw.rect(screen, "red", rect)


def draw_rectangle(screen: pygame.Surface):
    """Draw just the rectangle border, as specified"""
    rect = pygame.Rect((60, 10), (20, 30))  # explicit left/top, width/height tuples
    pygame.draw.rect(screen, "red", rect, width=3, border_radius=5)


def draw_filled_polygon(screen: pygame.Surface):
    # the polygon area is determined by a sequence of points
    vertices = ((120, 10), (160, 10), (140, 90))
    pygame.draw.polygon(screen, "green", vertices)


def draw_polygon(screen: pygame.Surface):
    """Draw just the polygon border, as specified"""
    points = ((180, 10), (220, 10), (200, 90))
    pygame.draw.polygon(screen, "green", points, width=1)


def draw_pixel_classic(screen: pygame.Surface):
    """OK for few pixels"""
    for i in range(255):
        for j in range(255):
            # setting the pixel in the given position to the given color
            screen.set_at((265 + i, 10 + j), (255, i, j))


def draw_pixel_rect(screen: pygame.Surface):
    """Uncommon, don't do it"""
    for i in range(255):
        for j in range(255):
            # filling with the passed color the rectangle sized (1, 1)
            screen.fill((i, j, 255), (10 + i, 265 + j, 1, 1))


def draw_pixel_modern(screen: pygame.Surface):
    """OK for few pixels"""
    for i in range(255):
        for j in range(255):
            # pick on screen the x, y pixel, set it with the given color
            pygame.gfxdraw.pixel(screen, 265 + i, 265 + j, (i, 255, j))


# noinspection DuplicatedCode
def handle_events() -> bool:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True


if __name__ == "__main__":
    pygame.init()

    try:
        main()
    finally:
        pygame.quit()
        print("Done.")
