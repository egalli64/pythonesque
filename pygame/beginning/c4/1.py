"""
All the RGB colors in a single image

From: Beginnning Python Games Development with PyGame - https://link.springer.com/book/10.1007/978-1-4842-0970-7
My reviewed version: https://github.com/egalli64/pythonesque/pygame/beginning
"""

import pygame

SCREEN_SIZE = (640, 480)
IMAGE_SIZE = (4096, 4096)
IMAGE_DEPTH = 24
IMAGE_NAME = "allcolors.bmp"

pygame.init()

screen = pygame.display.set_mode(SCREEN_SIZE)

# force the given depth to the surface (usually left to pygame to decide)
image = pygame.Surface(IMAGE_SIZE, depth=IMAGE_DEPTH)

# it takes some time
print("Looping, please wait ...")
for r in range(256):
    x = (r & 15) * 256
    y = (r >> 4) * 256
    for g in range(256):
        for b in range(256):
            # set a single pixel (not commonly used - too slow)
            image.set_at((x + g, y + b), (r, g, b))
print("Done")

pygame.image.save(image, IMAGE_NAME)

pygame.quit()
