"""
Illusion of Depth

From: Beginnning Python Games Development with PyGame - https://link.springer.com/book/10.1007/978-1-4842-0970-7
My reviewed version: https://github.com/egalli64/pythonesque/pygame/beginning
"""

import pygame
import random

FPS = 60

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
SCREEN_SIZE = pygame.Vector2(SCREEN_WIDTH, SCREEN_HEIGHT)

STAR_COLOR = (255, 255, 255)  # white
BACKGROUND_COLOR = (0, 0, 0)  # black


class Star:
    def __init__(self, x):
        self.x = x
        self.y = random.randrange(0, SCREEN_HEIGHT)
        self.speed = random.randint(10, 300)


def run():
    pygame.init()

    screen = pygame.display.set_mode(SCREEN_SIZE)
    clock = pygame.time.Clock()

    stars = []
    # Add a few stars for the first frame
    for _ in range(200):
        stars.append(Star(random.randrange(SCREEN_WIDTH)))

    running = True
    while running:
        td = clock.tick(FPS) / 1000

        # Add a new star
        star = Star(SCREEN_WIDTH)
        stars.append(star)

        # Remove stars that are no longer visible
        stars = list(filter(lambda star: star.x > 0, stars))

        screen.fill(BACKGROUND_COLOR)

        # Draw the stars
        for star in stars:
            x = star.x - td * star.speed
            pygame.draw.line(screen, STAR_COLOR, (x, star.y), (star.x + 1.0, star.y))
            star.x = x

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type in [pygame.QUIT, pygame.KEYDOWN]:
                running = False


if __name__ == "__main__":
    run()
    print("Done.")
    pygame.quit()
