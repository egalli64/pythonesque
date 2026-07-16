"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Sprite collisions
"""
from enum import Enum
import pygame

from target import Target
from probe import Probe, Direction

FPS = 30
BACKGROUND_COLOR = "white"
FONT_SIZE = 24
MODE_INFO_COLOR = "blue"
MODE_INFO_SHIFT = (-10, -10)


class Mode(Enum):
    RECT = pygame.K_r
    CIRCLE = pygame.K_c
    MASK = pygame.K_m


Mode.reverse_map = {member.value: member for member in Mode}


def as_direction(keys: pygame.key.ScancodeWrapper) -> Direction:
    if keys[pygame.K_LEFT]:
        return Direction.LEFT
    elif keys[pygame.K_RIGHT]:
        return Direction.RIGHT
    elif keys[pygame.K_UP]:
        return Direction.UP
    elif keys[pygame.K_DOWN]:
        return Direction.DOWN
    else:
        return Direction.STOP


class Game:
    mode: Mode
    mode_surf: pygame.Surface
    mode_rect: pygame.Rect

    @classmethod
    def load_resources(cls) -> None:
        cls._font = pygame.font.Font(None, FONT_SIZE)

    def __init__(self, window: pygame.Window, screen: pygame.Surface) -> None:
        self.window = window
        self.screen = screen
        self.viewport = screen.get_rect()

        self.probe = Probe(self.viewport)
        self.probe_group = pygame.sprite.GroupSingle(self.probe)

        self.targets = pygame.sprite.Group[Target](
            Target(self.viewport.centery, Target.Kind.BRICK),
            Target(self.viewport.centery, Target.Kind.SHIP),
            Target(self.viewport.centery, Target.Kind.ALIEN))

        self.place_targets()
        self.set_mode(Mode.RECT)
        self.running = True

    def place_targets(self) -> None:
        targets_width = sum(s.rect.width for s in self.targets)
        padding = (self.viewport.width - targets_width) // (len(self.targets) + 1)

        x = padding
        for target in self.targets:
            target.rect.left = x
            x = target.rect.right + padding

    def set_mode(self, mode: Mode) -> None:
        self.mode = mode
        self.mode_surf = Game._font.render(f"Mode: {self.mode.name}", True, MODE_INFO_COLOR)
        self.mode_rect = self.mode_surf.get_rect(bottomright=self.viewport.bottomright).move(MODE_INFO_SHIFT)

    def run(self) -> None:
        clock = pygame.time.Clock()

        while self.running:
            dt = clock.tick(FPS) / 1000

            self.handle_events()
            self.update(dt)
            self.draw()

    def handle_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                elif mode := Mode.reverse_map.get(event.key):
                    self.set_mode(mode)

        keys = pygame.key.get_pressed()
        self.probe.set_direction(as_direction(keys))

    def collide(self):
        for target in self.targets:
            match self.mode:
                case Mode.CIRCLE:
                    colliding = pygame.sprite.collide_circle(self.probe, target)
                case Mode.MASK:
                    colliding = bool(pygame.sprite.collide_mask(self.probe, target))
                case _:
                    colliding = pygame.sprite.collide_rect(self.probe, target)

            target.highlight(colliding)

    def alt_collide(self) -> None:
        """Using spritecollide() is not worthy here, better using directly the required collide function"""
        match self.mode:
            case Mode.CIRCLE:
                func = pygame.sprite.collide_circle
            case Mode.MASK:
                func = lambda s1, s2: bool(pygame.sprite.collide_mask(s1, s2))
            case _:
                func = pygame.sprite.collide_rect

        sprites = pygame.sprite.spritecollide(self.probe, self.targets, False, func)
        for target in self.targets:
            target.highlight(target in sprites)

    def update(self, dt: float) -> None:
        self.probe.update(dt)
        self.collide()
        # self.alt_collide()

    def draw(self) -> None:
        self.screen.fill(BACKGROUND_COLOR)
        self.targets.draw(self.screen)
        self.probe_group.draw(self.screen)

        self.screen.blit(self.mode_surf, self.mode_rect)
        self.window.flip()
