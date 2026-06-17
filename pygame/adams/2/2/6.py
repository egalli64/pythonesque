"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Particle swarm /6
"""

from random import randint
import pygame

FPS = 30
TITLE = "Particle swarm /6"
WIN_SIZE = (300, 600)
WIN_POS = (10, 50)
BACKGROUND_COLOR = "white"


class Circle:
    GRAVITY = 0.3
    RADIUS_DELTA = -0.1

    def __init__(self, pos) -> None:
        self.pos = pygame.Vector2(pos[0] + randint(-4, 4), pos[1] + randint(-4, 4))
        self.color = [randint(100, 255), randint(50, 255), 0]
        self.speed = pygame.Vector2(randint(-15, 15) / 10.01, randint(-100, 0) / 10.01)
        self.radius = 8.0

    def __repr__(self):
        return f"Circle(pos={self.pos}, color={self.color}, speed={self.speed}, radius={self.radius})"

    def update(self) -> None:
        """Change the circle vertical speed, position, and radius"""
        self.speed.y += Circle.GRAVITY
        self.pos += self.speed
        self.radius += self.RADIUS_DELTA

    def is_lost(self) -> bool:
        """
        Check if the current circle is escaped from the window (left, right, or down),
        or it is too small to be seen
        """
        if self.pos.x + self.radius < 0:
            return True
        elif self.pos.x - self.radius > WIN_SIZE[0]:
            return True
        elif self.pos.y - self.radius > WIN_SIZE[1]:
            return True
        elif self.radius < 1:
            return True
        return False

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, self.color, self.pos, self.radius)


def main():
    window = pygame.Window(TITLE, WIN_SIZE, WIN_POS)
    screen = window.get_surface()
    clock = pygame.time.Clock()
    circles = []

    while handle_events():
        clock.tick(FPS)

        if pygame.mouse.get_pressed()[0]:
            for _ in range(5):
                circles.append(Circle(pygame.mouse.get_pos()))

        for circle in circles:
            circle.update()
        circles = [circle for circle in circles if not circle.is_lost()]

        screen.fill(BACKGROUND_COLOR)
        for circle in circles:
            circle.draw(screen)
        window.flip()


def handle_events() -> bool:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True


if __name__ == "__main__":
    pygame.init()

    try:
        main()
    finally:
        pygame.quit()
        print("Done.")
