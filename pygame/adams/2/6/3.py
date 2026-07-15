"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Polling key status - key.get_pressed()
"""
from enum import Enum
from typing import override
import pygame

TITLE = "Keyboard to move"
WIN_SIZE = (300, 500)
WIN_POS = (50, 50)


class Defender(pygame.sprite.Sprite):
    class Direction(Enum):
        RIGHT = pygame.Vector2(1, 0)
        LEFT = pygame.Vector2(-1, 0)
        UP = pygame.Vector2(0, -1)
        DOWN = pygame.Vector2(0, 1)
        STOP = pygame.Vector2(0, 0)

    class Speed(Enum):  # pixel/second
        SLOW = 10
        NORMAL = 100
        FAST = 300

    FILENAME = "../images/defender.png"
    SIZE = (30, 30)

    image: pygame.Surface
    rect: pygame.FRect

    @classmethod
    def load_resources(cls):
        image = pygame.image.load(cls.FILENAME).convert_alpha()
        cls._image = pygame.transform.scale(image, cls.SIZE)

    def __init__(self, viewport: pygame.Rect) -> None:
        super().__init__()

        self.image = Defender._image
        self.rect = pygame.FRect(self.image.get_rect())
        self.rect.center = viewport.center

        self.viewport = viewport
        self.speed = Defender.Speed.NORMAL
        self.direction = Defender.Direction.STOP

    def set_direction(self, direction: Direction) -> None:
        self.direction = direction

    def set_speed(self, speed: Speed) -> None:
        self.speed = speed

    @override
    def update(self, dt: float) -> None:
        self.rect.move_ip(self.direction.value * self.speed.value * dt)
        self.rect.clamp_ip(self.viewport)


def direction_from_keys(keys: pygame.key.ScancodeWrapper) -> Defender.Direction:
    if keys[pygame.K_LEFT]:
        return Defender.Direction.LEFT
    elif keys[pygame.K_RIGHT]:
        return Defender.Direction.RIGHT
    elif keys[pygame.K_UP]:
        return Defender.Direction.UP
    elif keys[pygame.K_DOWN]:
        return Defender.Direction.DOWN
    else:
        return Defender.Direction.STOP


def speed_from_keys(keys: pygame.key.ScancodeWrapper) -> Defender.Speed:
    if keys[pygame.K_LSHIFT]:
        return Defender.Speed.FAST
    elif keys[pygame.K_RSHIFT]:
        return Defender.Speed.SLOW
    else:
        return Defender.Speed.NORMAL


class Game:
    FPS = 30
    BACKGROUND_COLOR = "white"

    def __init__(self, window: pygame.Window, screen: pygame.Surface) -> None:
        self.window = window
        self.screen = screen

        self.defender = Defender(screen.get_rect())
        self.defender_group = pygame.sprite.GroupSingle(self.defender)
        self.running = True

    def run(self) -> None:
        clock = pygame.time.Clock()

        while self.running:
            dt = clock.tick(Game.FPS) / 1000

            self.handle_events()
            self.defender_group.update(dt)
            self.draw()

    def handle_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.running = False

        # continuous events - poll the current keyboard state once per frame
        keys = pygame.key.get_pressed()
        self.defender.set_direction(direction_from_keys(keys))
        self.defender.set_speed(speed_from_keys(keys))

    def draw(self) -> None:
        self.screen.fill(Game.BACKGROUND_COLOR)
        self.defender_group.draw(self.screen)
        self.window.flip()


# noinspection DuplicatedCode
if __name__ == "__main__":
    pygame.init()
    pg_window = pygame.Window(TITLE, WIN_SIZE, WIN_POS)
    pg_screen = pg_window.get_surface()

    Defender.load_resources()

    try:
        Game(pg_window, pg_screen).run()
    finally:
        pygame.quit()
        print("Done.")
