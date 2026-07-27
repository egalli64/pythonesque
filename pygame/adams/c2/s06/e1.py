"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Control direction by keys
"""
from enum import Enum
from typing import override
import pygame

TITLE = "Detecting key down and up"
WIN_SIZE = (300, 600)
WIN_POS = (10, 50)
FPS = 30
BACKGROUND_COLOR = "white"


class Defender(pygame.sprite.Sprite):
    class Direction(Enum):
        STOP = pygame.Vector2(0, 0)
        RIGHT = pygame.Vector2(1, 0)
        LEFT = pygame.Vector2(-1, 0)
        UP = pygame.Vector2(0, -1)
        DOWN = pygame.Vector2(0, 1)

    FILENAME = "../images/defender.png"
    SIZE = (30, 30)
    SPEED = 100  # pixel/second

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
        self.direction = Defender.Direction.STOP

    def set_direction(self, direction: Direction) -> None:
        self.direction = direction

    @override
    def update(self, dt: float) -> None:
        self.rect.move_ip(self.direction.value * Defender.SPEED * dt)
        self.rect.clamp_ip(self.viewport)


class Game:
    def __init__(self, window: pygame.Window, screen: pygame.Surface) -> None:
        self.window = window
        self.screen = screen

        rect = self.screen.get_rect()
        self.defender = Defender(rect)
        self.defender_group = pygame.sprite.GroupSingle(self.defender)
        self.running = True

    def run(self) -> None:
        clock = pygame.time.Clock()

        while self.running:
            dt = clock.tick(FPS) / 1000

            self.handle_events()
            self.defender_group.update(dt)
            self.draw()

    def handle_events(self) -> None:
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    self.running = False
                case pygame.KEYDOWN:
                    match event.key:
                        case pygame.K_ESCAPE:
                            self.running = False
                        # see key.get_pressed() for a more robust approach
                        case pygame.K_RIGHT:
                            self.defender.set_direction(Defender.Direction.RIGHT)
                        case pygame.K_LEFT:
                            self.defender.set_direction(Defender.Direction.LEFT)
                        case pygame.K_UP:
                            self.defender.set_direction(Defender.Direction.UP)
                        case pygame.K_DOWN:
                            self.defender.set_direction(Defender.Direction.DOWN)
                case pygame.KEYUP:
                    # see key.get_pressed() for a more robust approach
                    if event.key in (pygame.K_RIGHT, pygame.K_LEFT, pygame.K_UP, pygame.K_DOWN):
                        self.defender.set_direction(Defender.Direction.STOP)

    def draw(self) -> None:
        self.screen.fill(BACKGROUND_COLOR)
        self.defender_group.draw(self.screen)
        self.window.flip()


# noinspection DuplicatedCode
if __name__ == "__main__":
    pygame.init()
    try:
        main_window = pygame.Window(TITLE, WIN_SIZE, WIN_POS)
        main_surface = main_window.get_surface()

        Defender.load_resources()

        Game(main_window, main_surface).run()
    finally:
        pygame.quit()
