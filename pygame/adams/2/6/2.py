"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Modifier keys - shift
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

    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.image.load(Defender.IMAGE).convert_alpha()
        self.image = pygame.transform.scale(self.image, Defender.SIZE)
        self.rect: pygame.FRect = pygame.FRect(self.image.get_rect())
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

    KEY_TO_DIRECTION = {
        pygame.K_LEFT: Defender.Direction.LEFT,
        pygame.K_RIGHT: Defender.Direction.RIGHT,
        pygame.K_UP: Defender.Direction.UP,
        pygame.K_DOWN: Defender.Direction.DOWN,
    }

    def __init__(self) -> None:
        self.window = pygame.Window(Game.TITLE, WIN_RECT.size, Game.WIN_POS)
        self.screen = self.window.get_surface()
        self.clock = pygame.time.Clock()

        self.defender = Defender()
        self.defender_group = pygame.sprite.GroupSingle(self.defender)

    def run(self) -> None:
        while self.handle_events():
            dt = self.clock.tick(Game.FPS) / 1000
            self.defender.update(dt)
            self.draw()

    def handle_events(self) -> bool:
        """Run the event loops, return False in case of termination request"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.mod == pygame.KMOD_NONE:
                    self.defender.set_speed(Defender.Speed.NORMAL)
                else:
                    if event.mod & pygame.KMOD_LSHIFT:
                        self.defender.set_speed(Defender.Speed.FAST)
                    if event.mod & pygame.KMOD_RSHIFT:
                        self.defender.set_speed(Defender.Speed.SLOW)
                if event.key == pygame.K_ESCAPE:
                    return False
                elif event.key in Game.KEY_TO_DIRECTION:
                    self.defender.set_direction(Game.KEY_TO_DIRECTION[event.key])
            elif event.type == pygame.KEYUP:
                # see key.get_pressed() for a more robust approach
                self.defender.set_speed(Defender.Speed.NORMAL)
                if event.key in Game.KEY_TO_DIRECTION:
                    self.defender.set_direction(Defender.Direction.STOP)
        return True

    def draw(self) -> None:
        self.screen.fill(Game.BACKGROUND_COLOR)
        self.defender_group.draw(self.screen)
        self.window.flip()


if __name__ == "__main__":
    pygame.init()

    try:
        Game().run()
    finally:
        pygame.quit()
        print("Done.")
