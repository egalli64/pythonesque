"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Particle swarm /3
"""

from random import randint

import pygame

FPS = 30

TITLE = "Particle swarm /3"
WIN_SIZE = (300, 600)
WIN_POS = (10, 50)
BACKGROUND_COLOR = "white"


class Circle:
    GRAVITY = 0.3
    RADIUS = 2

    def __init__(self, pos) -> None:
        self.pos = pygame.Vector2(pos[0] + randint(-2, 2), pos[1] + randint(-2, 2))
        self.color = (randint(100, 255), randint(50, 255), 0)
        self.speedy = randint(-100, 0) / 10.01

    def update(self) -> None:
        self.speedy += Circle.GRAVITY
        self.pos.y += self.speedy

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, self.color, self.pos, Circle.RADIUS)


def main():
    pygame.init()
    window = pygame.Window(TITLE, WIN_SIZE, WIN_POS)
    screen = window.get_surface()
    clock = pygame.time.Clock()
    circles = []

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if pygame.mouse.get_pressed()[0]:
            circles.append(Circle(pygame.mouse.get_pos()))

        for circle in circles:
            circle.update()

        screen.fill(BACKGROUND_COLOR)

        for circle in circles:
            circle.draw(screen)

        window.flip()
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
    print("Done.")
