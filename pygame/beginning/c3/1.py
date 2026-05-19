"""
Hello PyGame World

From: Beginnning Python Games Development with PyGame - https://link.springer.com/book/10.1007/978-1-4842-0970-7
My reviewed version: https://github.com/egalli64/pythonesque/pygame/beginning
"""

import pygame

BACKGROUND_IMG = "pygame/beginning/img/sushiplate.jpg"
MOUSE_IMG = "pygame/beginning/img/fugu.png"
SCREEN_SIZE = (640, 480)

pygame.init()

screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Hello, World!")
# get rid of the standard mouse image
pygame.mouse.set_visible(False)

# plain image load
background = pygame.image.load(BACKGROUND_IMG).convert()
# image load preserving alpha information
mouse_cursor = pygame.image.load(MOUSE_IMG).convert_alpha()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
        else:
            # implicitly copy background to screen at (0, 0) position
            screen.blit(background)

            # get the mouse position, center the mouse cursor image, copy it to screen
            x, y = pygame.mouse.get_pos()
            x -= mouse_cursor.get_width() / 2
            y -= mouse_cursor.get_height() / 2
            screen.blit(mouse_cursor, (x, y))

            # full screen update
            pygame.display.flip()
