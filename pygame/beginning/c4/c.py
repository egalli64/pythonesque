"""
Ellipse

From: Beginning Python Games Development with PyGame - https://link.springer.com/book/10.1007/978-1-4842-0970-7
My reviewed version: https://github.com/egalli64/pythonesque folder pygame/beginning
"""
import pygame

SCREEN_SIZE = (640, 480)
BACKGROUND_COLOR = (255, 255, 255)
ELLIPSE_COLOR = (0, 255, 0)

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BACKGROUND_COLOR)
    pygame.draw.ellipse(screen, ELLIPSE_COLOR, (0, 0, *pygame.mouse.get_pos()))
    pygame.display.flip()

pygame.quit()
