"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Modifier keys - shift
"""
from enum import Enum
from typing import override
import pygame

TITLE = "Keyboard with shift"
WIN_SIZE = (300, 600)
WIN_POS = (10, 50)


class Defender(pygame.sprite.Sprite):
    class Direction(Enum):
        STOP = pygame.Vector2(0, 0)
        RIGHT = pygame.Vector2(1, 0)
        LEFT = pygame.Vector2(-1, 0)
        UP = pygame.Vector2(0, -1)
        DOWN = pygame.Vector2(0, 1)

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


class Game:
    FPS = 30
    BACKGROUND_COLOR = "white"

    KEY_TO_DIRECTION = {
        pygame.K_LEFT: Defender.Direction.LEFT,
        pygame.K_RIGHT: Defender.Direction.RIGHT,
        pygame.K_UP: Defender.Direction.UP,
        pygame.K_DOWN: Defender.Direction.DOWN,
    }

    def __init__(self, window: pygame.Window, screen: pygame.Surface) -> None:
        self.window = window
        self.screen = screen

        self.defender = Defender(self.screen.get_rect())
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
            elif event.type == pygame.KEYDOWN:
                # check the modifiers bit mask
                if event.mod & pygame.KMOD_LSHIFT:
                    self.defender.set_speed(Defender.Speed.FAST)
                elif event.mod & pygame.KMOD_RSHIFT:
                    self.defender.set_speed(Defender.Speed.SLOW)
                else:
                    self.defender.set_speed(Defender.Speed.NORMAL)

                if event.key == pygame.K_ESCAPE:
                    self.running = False
                elif event.key in Game.KEY_TO_DIRECTION:
                    self.defender.set_direction(Game.KEY_TO_DIRECTION[event.key])
            elif event.type == pygame.KEYUP:
                # see key.get_pressed() for a more robust approach
                if event.key in (pygame.K_LSHIFT, pygame.K_RSHIFT):
                    self.defender.set_speed(Defender.Speed.NORMAL)
                elif event.key in Game.KEY_TO_DIRECTION:
                    self.defender.set_direction(Defender.Direction.STOP)

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
