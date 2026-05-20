"""
Full screen

From: Beginnning Python Games Development with PyGame - https://link.springer.com/book/10.1007/978-1-4842-0970-7
My reviewed version: https://github.com/egalli64/pythonesque/pygame/beginning
"""

import pygame

BACKGROUND_IMG = "pygame/beginning/img/sushiplate.jpg"
SCREEN_SIZE = (640, 480)


pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
image = pygame.image.load(BACKGROUND_IMG).convert()
fullscreen = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_f:
            fullscreen = not fullscreen
            flags = pygame.FULLSCREEN if fullscreen else 0
            screen = pygame.display.set_mode(SCREEN_SIZE, flags)

        screen.blit(image)
        pygame.display.flip()

print("Done!")
pygame.quit()
