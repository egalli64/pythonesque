"""
Blending colors by lerping

From: Beginnning Python Games Development with PyGame - https://link.springer.com/book/10.1007/978-1-4842-0970-7
My reviewed version: https://github.com/egalli64/pythonesque/pygame/beginning
"""

import pygame

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
BLEND_AREA = (0, SCREEN_HEIGHT // 2, 640, SCREEN_HEIGHT // 2)
BACKGROUND_COLOR = (255, 255, 255)  # white
TRIANGLE_COLOR = (0, 255, 0)  # green
TRIANGLE_VERTICES = ((0, 120), (639, 100), (639, 140))
CIRCLE_COLOR = (0, 0, 0)  # black
CIRCLE_RADIUS = 10
LEFT_COLOR = (221, 99, 20)  # burnt orange
RIGHT_COLOR = (96, 130, 51)  # olive green

pygame.init()

screen = pygame.display.set_mode(SCREEN_SIZE)


def blend_color(factor):
    """Blend colors using the given factor"""
    red = int(LEFT_COLOR[0] + (RIGHT_COLOR[0] - LEFT_COLOR[0]) * factor)
    green = int(LEFT_COLOR[1] + (RIGHT_COLOR[1] - LEFT_COLOR[1]) * factor)
    blue = int(LEFT_COLOR[2] + (RIGHT_COLOR[2] - LEFT_COLOR[2]) * factor)
    return red, green, blue


factor = 0.0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    else:
        screen.fill(BACKGROUND_COLOR)

        pygame.draw.polygon(screen, TRIANGLE_COLOR, TRIANGLE_VERTICES)
        circle_pos = (factor * SCREEN_WIDTH, SCREEN_HEIGHT // 4)
        pygame.draw.circle(screen, CIRCLE_COLOR, circle_pos, CIRCLE_RADIUS)

        x, y = pygame.mouse.get_pos()
        # clamp x to the screen width
        x = max(0, min(x, SCREEN_WIDTH))

        if pygame.mouse.get_pressed()[0]:
            factor = x / SCREEN_WIDTH
            pygame.display.set_caption(f"PyGame Color Blend Test: {factor:.3f}")

        pygame.draw.rect(screen, blend_color(factor), BLEND_AREA)

        pygame.display.flip()

print("Done")
pygame.quit()
