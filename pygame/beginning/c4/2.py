"""
Choose a color

From: Beginnning Python Games Development with PyGame - https://link.springer.com/book/10.1007/978-1-4842-0970-7
My reviewed version: https://github.com/egalli64/pythonesque/pygame/beginning
"""

import pygame

SCREEN_SIZE = (640, 480)
SCALE_HEIGHT = 80
SCALE_SIZE = (640, SCALE_HEIGHT)
RED_SCALE_XY = (0, 0)
GREEN_SCALE_XY = (0, SCALE_HEIGHT)
BLUE_SCALE_XY = (0, SCALE_HEIGHT * 2)
RESULT_SIZE = (0, 240, 640, 240)
CIRCLE_COLOR = (255, 255, 255)  # white

pygame.init()

screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)


def create_scales():
    """Create images with smooth gradients"""
    red_scale = pygame.surface.Surface(SCALE_SIZE)
    green_scale = pygame.surface.Surface(SCALE_SIZE)
    blue_scale = pygame.surface.Surface(SCALE_SIZE)

    for x in range(640):
        c = int(x / 639 * 255)
        red = (c, 0, 0)
        green = (0, c, 0)
        blue = (0, 0, c)
        line_rect = pygame.Rect(x, 0, 1, SCALE_HEIGHT)
        pygame.draw.rect(red_scale, red, line_rect)
        pygame.draw.rect(green_scale, green, line_rect)
        pygame.draw.rect(blue_scale, blue, line_rect)
    return red_scale, green_scale, blue_scale


red_scale, green_scale, blue_scale = create_scales()

color = [127, 127, 127]  # gray

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        else:
            # Draw the scales to the screen
            screen.blit(red_scale, RED_SCALE_XY)
            screen.blit(green_scale, GREEN_SCALE_XY)
            screen.blit(blue_scale, BLUE_SCALE_XY)

            x, y = pygame.mouse.get_pos()
            # for safety, clamp x to [0, SCREEN_SIZE[0]]
            x = max(0, min(x, SCREEN_SIZE[0]))

            # If the mouse was pressed on one of the sliders, adjust the color component
            if pygame.mouse.get_pressed()[0]:
                for scale in range(3):
                    if scale * SCALE_HEIGHT < y < (scale + 1) * SCALE_HEIGHT:
                        color[scale] = int(x / 639 * 255)
                pygame.display.set_caption("Color Test: " + str(color))

            # Draw a circle for each slider to represent the current setting
            for scale in range(3):
                pos = (color[scale] / 255 * 639, scale * SCALE_HEIGHT + 40)
                pygame.draw.circle(screen, CIRCLE_COLOR, pos, 20)

            pygame.draw.rect(screen, color, RESULT_SIZE)

            pygame.display.flip()


print("Done.")
pygame.quit()
