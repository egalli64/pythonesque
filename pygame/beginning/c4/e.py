"""
Line

From: Beginning Python Games Development with PyGame - https://link.springer.com/book/10.1007/978-1-4842-0970-7
My reviewed version: https://github.com/egalli64/pythonesque folder pygame/beginning
"""
import pygame

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

BACKGROUND_COLOR = (255, 255, 255)
LINE_COLOR = (0, 0, 0)

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        screen.fill(BACKGROUND_COLOR)

        pos = pygame.mouse.get_pos()

        for x in range(0, SCREEN_WIDTH, 40):
            pygame.draw.line(screen, LINE_COLOR, (x, 0), pos)
            pygame.draw.line(screen, LINE_COLOR, (x, SCREEN_HEIGHT), pos)

        for y in range(0, SCREEN_HEIGHT, 40):
            pygame.draw.line(screen, LINE_COLOR, (0, y), pos)
            pygame.draw.line(screen, LINE_COLOR, (SCREEN_WIDTH, y), pos)

        pygame.display.flip()

pygame.quit()
