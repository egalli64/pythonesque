"""
Choose a color

From: Beginning Python Games Development with PyGame - https://link.springer.com/book/10.1007/978-1-4842-0970-7
My reviewed version: https://github.com/egalli64/pythonesque folder pygame/beginning
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
CIRCLE_COLOR = (255, 255, 255)

pygame.init()

screen = pygame.display.set_mode(SCREEN_SIZE)


def scale_color_channel(value: int):
    """scaling the color in [0, 255] for the screen width"""
    assert 0 <= value <= SCREEN_WIDTH
    return int(value / (SCREEN_WIDTH - 1) * MAX_CHANNEL_INTENSITY)


def create_scales():
    """Create images with smooth gradients"""
    red_image = pygame.surface.Surface(SCALE_SIZE)
    green_image = pygame.surface.Surface(SCALE_SIZE)
    blue_image = pygame.surface.Surface(SCALE_SIZE)

    for i in range(SCREEN_WIDTH):
        scaled_channel = scale_color_channel(i)
        red = (scaled_channel, 0, 0)
        green = (0, scaled_channel, 0)
        blue = (0, 0, scaled_channel)
        line_rect = pygame.Rect(i, 0, 1, SCALE_HEIGHT)
        pygame.draw.rect(red_image, red, line_rect)
        pygame.draw.rect(green_image, green, line_rect)
        pygame.draw.rect(blue_image, blue, line_rect)
    return red_image, green_image, blue_image


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

pygame.quit()
