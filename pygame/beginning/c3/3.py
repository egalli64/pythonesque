"""
Key events

From: Beginnning Python Games Development with PyGame - https://link.springer.com/book/10.1007/978-1-4842-0970-7
My reviewed version: https://github.com/egalli64/pythonesque/pygame/beginning
"""

import pygame

BACKGROUND_IMG = "pygame/beginning/img/sushiplate.jpg"
BACKGROUND_COLOR = (0, 0, 0)
SCREEN_SIZE = (640, 480)


pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
image = pygame.image.load(BACKGROUND_IMG).convert()

x, y = 0, 0
move_x, move_y = 0, 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # move the image by one pixel in the specified position
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move_x = -1
            elif event.key == pygame.K_RIGHT:
                move_x = +1
            elif event.key == pygame.K_UP:
                move_y = -1
            elif event.key == pygame.K_DOWN:
                move_y = +1

            x += move_x
            y += move_y
        # reset the deltas
        elif event.type == pygame.KEYUP:
            move_x = 0
            move_y = 0

        screen.fill(BACKGROUND_COLOR)
        screen.blit(image, (x, y))

        pygame.display.flip()

print("Done!")
pygame.quit()
