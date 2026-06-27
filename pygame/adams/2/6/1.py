"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Control direction by keys
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

    IMAGE = "../images/defender.png"
    SIZE = (30, 30)
    DEFAULT_SPEED = 100  # pixel/second

    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.image.load(Defender.IMAGE).convert_alpha()
        self.image = pygame.transform.scale(self.image, Defender.SIZE)
        self.rect: pygame.FRect = pygame.FRect(self.image.get_rect())
        self.rect.center = WIN_RECT.center
        self.speed = Defender.DEFAULT_SPEED
        self.direction = Defender.Direction.STOP

    def set_direction(self, direction: Direction):
        self.direction = direction

    @override
    def update(self, dt) -> None:
        self.rect.move_ip(self.direction.value * self.speed * dt)
        self.rect.clamp_ip(WIN_RECT)


class Game:
    FPS = 30
    TITLE = "Keyboard"
    WIN_POS = (10, 50)
    BACKGROUND_COLOR = "white"

    def __init__(self) -> None:
        self.window = pygame.Window(Game.TITLE, WIN_RECT.size, Game.WIN_POS)
        self.screen = self.window.get_surface()
        self.clock = pygame.time.Clock()

        self.defender = Defender()
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.defender)

    def run(self) -> None:
        while self.handle_events():
            dt = self.clock.tick(Game.FPS) / 1000
            self.all_sprites.update(dt)
            self.draw()

    def handle_events(self) -> bool:
        """Run the event loops, return False in case of termination request"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
                elif event.key == pygame.K_RIGHT:
                    self.defender.set_direction(Defender.Direction.RIGHT)
                elif event.key == pygame.K_LEFT:
                    self.defender.set_direction(Defender.Direction.LEFT)
                elif event.key == pygame.K_UP:
                    self.defender.set_direction(Defender.Direction.UP)
                elif event.key == pygame.K_DOWN:
                    self.defender.set_direction(Defender.Direction.DOWN)
            elif event.type == pygame.KEYUP:
                if event.key in (
                    pygame.K_RIGHT,
                    pygame.K_LEFT,
                    pygame.K_UP,
                    pygame.K_DOWN,
                ):
                    self.defender.set_direction(Defender.Direction.STOP)
        return True

    def draw(self) -> None:
        self.screen.fill(Game.BACKGROUND_COLOR)
        self.all_sprites.draw(self.screen)
        self.window.flip()


if __name__ == "__main__":
    pygame.init()

    try:
        Game().run()
    finally:
        pygame.quit()
        print("Done.")
