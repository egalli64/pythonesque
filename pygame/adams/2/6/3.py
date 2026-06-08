"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Polling key status - key.get_pressed()
"""

from enum import Enum
from typing import override
import pygame

WIN_RECT = pygame.Rect(0, 0, 300, 600)


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

    IMAGE = "../images/defender.png"
    SIZE = (30, 30)

    rect: pygame.FRect
    image: pygame.Surface

    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.image.load(Defender.IMAGE).convert_alpha()
        self.image = pygame.transform.scale(self.image, Defender.SIZE)  # type: ignore
        self.rect = pygame.FRect(self.image.get_rect())  # type: ignore
        self.rect.center = WIN_RECT.center
        self.speed = Defender.Speed.NORMAL
        self.direction = Defender.Direction.STOP

    def set_direction(self, direction: Direction):
        self.direction = direction

    def set_speed(self, speed: Speed):
        self.speed = speed

    @override
    def update(self, dt) -> None:
        self.rect.move_ip(self.direction.value * self.speed.value * dt)
        self.rect.clamp_ip(WIN_RECT)


class Game(object):
    FPS = 30
    TITLE = "Keyboard"
    WIN_POS = (10, 50)
    BACKGROUND_COLOR = "white"

    def __init__(self) -> None:
        pygame.init()

        self.window = pygame.Window(Game.TITLE, WIN_RECT.size, Game.WIN_POS)
        self.screen = self.window.get_surface()
        self.clock = pygame.time.Clock()

        self.defender = Defender()
        self.defender_group = pygame.sprite.GroupSingle(self.defender)

    def run(self) -> None:
        while self.handle_events():
            dt = self.clock.tick(Game.FPS) / 1000
            self.update(dt)
            self.draw()

    def handle_events(self) -> bool:
        """Run the event loops, return False in case of termination request"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return False
        return True

    def get_direction(self, keys: pygame.key.ScancodeWrapper) -> Defender.Direction:
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

    def get_speed(self, keys: pygame.key.ScancodeWrapper) -> Defender.Speed:
        if keys[pygame.K_LSHIFT]:
            return Defender.Speed.FAST
        elif keys[pygame.K_RSHIFT]:
            return Defender.Speed.SLOW
        else:
            return Defender.Speed.NORMAL

    def update(self, dt):
        keys = pygame.key.get_pressed()

        self.defender.set_direction(self.get_direction(keys))
        self.defender.set_speed(self.get_speed(keys))

        self.defender.update(dt)

    def draw(self) -> None:
        self.screen.fill(Game.BACKGROUND_COLOR)
        self.defender_group.draw(self.screen)
        self.window.flip()


if __name__ == "__main__":
    Game().run()
    pygame.quit()
    print("Done.")
