"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Self add a Sprite to a Group + remove a sprite from any group having it
"""
from random import randint
from typing import override
import pygame

FPS = 30
TITLE = "Sprite group add and remove"
WIN_SIZE = (300, 600)
BACKGROUND_COLOR = "white"


class Ship(pygame.sprite.Sprite):
    FILENAME = "../images/defender.png"
    SIZE = (30, 30)
    Y_SPEED = 300  # pixel/second

    image: pygame.Surface
    rect: pygame.FRect

    @classmethod
    def load_resources(cls):
        image = pygame.image.load(cls.FILENAME).convert_alpha()
        cls._image = pygame.transform.scale(image, cls.SIZE)

    def __init__(self, pos: tuple[int, int], viewport: pygame.Rect, group: pygame.sprite.Group) -> None:
        super().__init__(group)

        self.image = Ship._image
        self.rect = pygame.FRect(self.image.get_rect())
        self.rect.bottomleft = pos

        self.viewport = viewport
        self.y_velocity = -Ship.Y_SPEED

    @override
    def update(self, dt: float) -> None:
        self.rect.move_ip(0, self.y_velocity * dt)
        if self.rect.bottom < self.viewport.centery:
            # misnomer: it just removes this sprite for any groups that owns it
            self.kill()


class Game:
    # as alternative see also time.set_timer() + user event
    SPAWN_DELAY = 2 / 3  # in seconds
    SHIP_MAX_LEFT = WIN_SIZE[0] - Ship.SIZE[0]

    def __init__(self, window: pygame.Window, screen: pygame.Surface) -> None:
        self.window = window
        self.screen = screen
        self.rect = screen.get_rect()

        self.ships = pygame.sprite.Group()
        self.running = True
        self.spawn_timer = 0

    def run(self) -> None:
        clock = pygame.time.Clock()

        while self.running:
            dt = clock.tick(FPS) / 1000

            self.handle_events()
            self.update(dt)
            self.draw()

    def handle_events(self) -> None:
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    self.running = False
                case pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False

    def update(self, dt: float) -> None:
        self.spawn_timer += dt
        if self.spawn_timer >= Game.SPAWN_DELAY:
            self.spawn_timer -= Game.SPAWN_DELAY
            spawn_pos = (randint(0, Game.SHIP_MAX_LEFT), WIN_SIZE[1])
            Ship(spawn_pos, self.rect, self.ships)

        self.ships.update(dt)

    def draw(self) -> None:
        self.screen.fill(BACKGROUND_COLOR)
        self.ships.draw(self.screen)
        self.window.flip()


if __name__ == "__main__":
    pygame.init()
    try:
        main_window = pygame.Window(TITLE, WIN_SIZE)
        main_surface = main_window.get_surface()

        Ship.load_resources()

        Game(main_window, main_surface).run()
    finally:
        pygame.quit()
