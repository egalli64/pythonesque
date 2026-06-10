"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Types of collision
"""

from enum import Enum
from typing import override
import pygame

WIN_RECT = pygame.Rect(0, 0, 700, 200)


class Target(pygame.sprite.Sprite):
    def __init__(self, filename: str, filename_hit: str) -> None:
        super().__init__()
        self.image_normal = pygame.image.load(filename).convert_alpha()
        self.image_hit = pygame.image.load(filename_hit).convert_alpha()
        self.image = self.image_normal
        self.rect: pygame.Rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.radius = self.rect.centerx
        self.rect.centery = WIN_RECT.centery

    @override
    def update(self, hit: bool) -> None:
        self.image = self.image_hit if hit else self.image_normal


class Probe(pygame.sprite.Sprite):
    START_POSITION = (10, 10)
    SPEED = 100

    class Direction(Enum):
        STOP = pygame.Vector2(0, 0)
        RIGHT = pygame.Vector2(1, 0)
        LEFT = pygame.Vector2(-1, 0)
        UP = pygame.Vector2(0, -1)
        DOWN = pygame.Vector2(0, 1)

    def __init__(self, filename: str) -> None:
        super().__init__()
        self.image = pygame.image.load(filename).convert_alpha()
        self.rect: pygame.Rect = self.image.get_rect()
        self.radius = self.rect.centery
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.center = Probe.START_POSITION
        self.direction = Probe.Direction.STOP.value

    @override
    def update(self, dt) -> None:
        self.rect.move_ip(Probe.SPEED * self.direction * dt)
        self.rect.clamp_ip(WIN_RECT)

    def set_direction(self, direction: Direction) -> None:
        self.direction = direction.value


class Game(object):
    FPS = 30
    TITLE = "Collision Types"
    BACKGROUND_COLOR = "white"

    PROBE = "images/shoot.png"
    BRICK = ("images/brick1.png", "images/brick2.png")
    SHIP = ("images/ship1.png", "images/ship2.png")
    ALIEN = ("images/alienbig1.png", "images/alienbig2.png")
    DEFAULT_MODE = "rect"

    INFO_POS = (10, WIN_RECT.bottom - 30)

    def __init__(self) -> None:
        self.window = pygame.Window(Game.TITLE, WIN_RECT.size)
        self.screen = self.window.get_surface()
        self.clock = pygame.time.Clock()

        self.font = pygame.font.Font(None, 24)
        self.probe = Probe(Game.PROBE)
        self.probe_group = pygame.sprite.GroupSingle(self.probe)

        self.all_targets = pygame.sprite.Group()
        self.all_targets.add(Target(*Game.BRICK))
        self.all_targets.add(Target(*Game.SHIP))
        self.all_targets.add(Target(*Game.ALIEN))
        self.mode = Game.DEFAULT_MODE

    def run(self) -> None:
        self.resize()
        while self.handle_events():
            dt = self.clock.tick(Game.FPS) / 1000

            self.update(dt)
            self.draw()

    def handle_events(self) -> bool:
        """Run the event loops, return False in case of termination request"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
                elif event.key == pygame.K_r:
                    self.mode = "rect"
                elif event.key == pygame.K_c:
                    self.mode = "circle"
                elif event.key == pygame.K_m:
                    self.mode = "mask"
        return True

    def collide(self, target: Target):
        if self.mode == "circle":
            return pygame.sprite.collide_circle(self.probe, target)
        elif self.mode == "mask":
            return pygame.sprite.collide_mask(self.probe, target)
        else:
            return pygame.sprite.collide_rect(self.probe, target)

    def update(self, dt) -> None:
        keys = pygame.key.get_pressed()
        self.probe.set_direction(self.get_direction(keys))
        self.probe.update(dt)

        for target in self.all_targets:
            target.update(self.collide(target))

    def draw(self) -> None:
        self.screen.fill(Game.BACKGROUND_COLOR)
        self.all_targets.draw(self.screen)
        self.probe_group.draw(self.screen)

        text_info = self.font.render(f"Mode: {self.mode}", True, "blue")
        self.screen.blit(text_info, Game.INFO_POS)

        self.window.flip()

    def resize(self) -> None:
        total_width = 0
        for s in self.all_targets:
            total_width += s.rect.width
        padding = (WIN_RECT.width - total_width) // 4
        for i in range(len(self.all_targets)):
            if i == 0:
                self.all_targets.sprites()[i].rect.left = padding
            else:
                self.all_targets.sprites()[i].rect.left = (
                    self.all_targets.sprites()[i - 1].rect.right + padding
                )

    def get_direction(self, keys: pygame.key.ScancodeWrapper) -> Probe.Direction:
        if keys[pygame.K_LEFT]:
            return Probe.Direction.LEFT
        elif keys[pygame.K_RIGHT]:
            return Probe.Direction.RIGHT
        elif keys[pygame.K_UP]:
            return Probe.Direction.UP
        elif keys[pygame.K_DOWN]:
            return Probe.Direction.DOWN
        else:
            return Probe.Direction.STOP


if __name__ == "__main__":
    pygame.init()

    try:
        Game().run()
    finally:
        pygame.quit()
        print("Done.")
