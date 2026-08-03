"""
Antialiased line

From: Beginning Python Games Development with PyGame - https://link.springer.com/book/10.1007/978-1-4842-0970-7
My reviewed version: https://github.com/egalli64/pythonesque folder pygame/beginning
"""
import pygame

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

BACKGROUND_COLOR = (255, 255, 255)
LINE_COLOR = (0, 255, 0)
AALINE_COLOR = (0, 0, 255)


pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)

screen.fill(BACKGROUND_COLOR)

pygame.draw.line(screen, LINE_COLOR, (0, 200), (SCREEN_WIDTH, 220))
pygame.draw.aaline(screen, AALINE_COLOR, (0, 220), (SCREEN_WIDTH, 240))

pygame.display.flip()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
