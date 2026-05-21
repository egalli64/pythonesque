"""
Make a color darker

From: Beginnning Python Games Development with PyGame - https://link.springer.com/book/10.1007/978-1-4842-0970-7
My reviewed version: https://github.com/egalli64/pythonesque/pygame/beginning
"""

import pygame

BLOCK_WIDTH = 640
BLOCK_HEIGHT = 240
BLOCK_SIZE = (BLOCK_WIDTH, BLOCK_HEIGHT)
SCREEN_SIZE = (BLOCK_WIDTH, BLOCK_HEIGHT * 2)

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)


def scale_color(color, scale):
    red, green, blue = color
    red = int(red * scale)
    green = int(green * scale)
    blue = int(blue * scale)
    return red, green, blue


original_color = (221, 99, 20)
print(original_color)
darker_color = scale_color(original_color, 0.5)
print(darker_color)

rect = pygame.Rect(0, 0, BLOCK_WIDTH, BLOCK_HEIGHT)

original = pygame.surface.Surface(BLOCK_SIZE)
pygame.draw.rect(original, original_color, rect)
screen.blit(original, (0, 0))

darker = pygame.surface.Surface(BLOCK_SIZE)
pygame.draw.rect(darker, darker_color, rect)
screen.blit(darker, (0, BLOCK_HEIGHT))

pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


print("Done.")
pygame.quit()
