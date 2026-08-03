"""
Polygon

From: Beginning Python Games Development with PyGame - https://link.springer.com/book/10.1007/978-1-4842-0970-7
My reviewed version: https://github.com/egalli64/pythonesque folder pygame/beginning
"""
import pygame

SCREEN_SIZE = (640, 480)
BACKGROUND_COLOR = (255, 255, 255)
POLYGON_COLOR = (0, 255, 0)
POINT_COLOR = (0, 0, 255)
POINT_RADIUS = 3

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
points = []

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            points.append(event.pos)

    screen.fill(BACKGROUND_COLOR)

    if len(points) >= 3:
        # filled polygon
        pygame.draw.polygon(screen, POLYGON_COLOR, points)
        # unfilled polygon, specify line thickness
        # pygame.draw.polygon(screen, POLYGON_COLOR, points, 5)
    for point in points:
        pygame.draw.circle(screen, POINT_COLOR, point, POINT_RADIUS)

    pygame.display.flip()

pygame.quit()
