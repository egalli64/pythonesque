"""
Choose a color

From: Beginnning Python Games Development with PyGame - https://link.springer.com/book/10.1007/978-1-4842-0970-7
My reviewed version: https://github.com/egalli64/pythonesque/pygame/beginning
"""

import pygame

SCREEN_WIDTH = 640
SCREEN_SIZE = (SCREEN_WIDTH, 480)
SCALE_HEIGHT = 80
SCALE_SIZE = (SCREEN_WIDTH, SCALE_HEIGHT)
RED_SCALE_XY = (0, 0)
GREEN_SCALE_XY = (0, SCALE_HEIGHT)
BLUE_SCALE_XY = (0, SCALE_HEIGHT * 2)
RESULT_AREA = (0, 240, SCREEN_WIDTH, 240)
MAX_CHANNEL_INTENSITY = 255
CIRCLE_COLOR = (255, 255, 255)  # white

pygame.init()

screen = pygame.display.set_mode(SCREEN_SIZE)


def scale_color_channel(x: int):
    """scaling the color in [0, 255] for the screen width"""
    assert 0 <= x <= SCREEN_WIDTH
    return int(x / (SCREEN_WIDTH - 1) * MAX_CHANNEL_INTENSITY)


def create_scales():
    """Create images with smooth gradients"""
    red_scale = pygame.surface.Surface(SCALE_SIZE)
    green_scale = pygame.surface.Surface(SCALE_SIZE)
    blue_scale = pygame.surface.Surface(SCALE_SIZE)

    for x in range(SCREEN_WIDTH):
        channel = scale_color_channel(x)
        red = (channel, 0, 0)
        green = (0, channel, 0)
        blue = (0, 0, channel)
        line_rect = pygame.Rect(x, 0, 1, SCALE_HEIGHT)
        pygame.draw.rect(red_scale, red, line_rect)
        pygame.draw.rect(green_scale, green, line_rect)
        pygame.draw.rect(blue_scale, blue, line_rect)
    return red_scale, green_scale, blue_scale


red_scale, green_scale, blue_scale = create_scales()

# initially the resulting color is gray
color = [127, 127, 127]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        else:
            screen.blit(red_scale, RED_SCALE_XY)
            screen.blit(green_scale, GREEN_SCALE_XY)
            screen.blit(blue_scale, BLUE_SCALE_XY)

            x, y = pygame.mouse.get_pos()
            # clamp x to the screen size
            x = max(0, min(x, SCREEN_SIZE[0]))

            # If the mouse was pressed on one of the sliders, adjust the color channel
            if pygame.mouse.get_pressed()[0]:
                for channel in range(3):
                    if channel * SCALE_HEIGHT < y < (channel + 1) * SCALE_HEIGHT:
                        color[channel] = scale_color_channel(x)
                pygame.display.set_caption("Color Test: " + str(color))

            # Draw a circle for each slider to represent the current setting
            for channel in range(3):
                x = color[channel] / MAX_CHANNEL_INTENSITY * (SCREEN_WIDTH - 1)
                y = channel * SCALE_HEIGHT + SCALE_HEIGHT // 2
                pygame.draw.circle(screen, CIRCLE_COLOR, (x, y), SCALE_HEIGHT // 4)

            pygame.draw.rect(screen, color, RESULT_AREA)

            pygame.display.flip()


print("Done.")
pygame.quit()
