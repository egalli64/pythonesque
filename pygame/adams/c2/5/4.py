"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Better encapsulation by class Game
"""
from typing import override
import pygame

TITLE = "The game orchestrator"
WIN_SIZE = (600, 100)
WIN_POS = (10, 50)


class Defender(pygame.sprite.Sprite):
    FILENAME = "../images/defender.png"
    SIZE = (30, 30)
    X_SPEED = 150  # pixel/second
    BOTTOM_GAP = 5

    image: pygame.Surface
    rect: pygame.FRect

    @classmethod
    def load_resources(cls):
        image = pygame.image.load(cls.FILENAME).convert_alpha()
        cls._image = pygame.transform.scale(image, cls.SIZE)

    def __init__(self, viewport: pygame.Rect) -> None:
        super().__init__()

        self.image = Defender._image
        self.rect: pygame.FRect = pygame.FRect(self.image.get_rect())
        self.rect.midbottom = viewport.centerx, viewport.bottom - Defender.BOTTOM_GAP
        self.x_velocity = Defender.X_SPEED

    def bounce(self, border: Border) -> None:
        if border.right:
            self.rect.right = border.rect.left
            self.x_velocity = -Defender.X_SPEED
        else:
            self.rect.left = border.rect.right
            self.x_velocity = Defender.X_SPEED

    @override
    def update(self, dt) -> None:
        self.rect.move_ip(self.x_velocity * dt, 0)


# noinspection DuplicatedCode
class Border(pygame.sprite.Sprite):
    FILENAME = "../images/brick.png"
    SIZE = (35, WIN_SIZE[1])

    image: pygame.Surface
    rect: pygame.Rect

    @classmethod
    def load_resources(cls):
        image = pygame.image.load(cls.FILENAME).convert_alpha()
        cls._image = pygame.transform.scale(image, cls.SIZE)

    def __init__(self, viewport: pygame.Rect, right: bool = False) -> None:
        super().__init__()

        self.image = Border._image
        self.rect = self.image.get_rect()
        self.right = right

        if right:
            self.rect.right = viewport.right
        else:
            self.rect.left = viewport.left


class Game:
    FPS = 30
    BACKGROUND_COLOR = "white"

    def __init__(self, window: pygame.Window, screen: pygame.Surface) -> None:
        self.window = window
        self.screen = screen
        self.viewport = screen.get_rect()
        self.running = True

        self.defender = Defender(self.viewport)
        self.borders = pygame.sprite.Group[Border](Border(self.viewport), Border(self.viewport, right=True))
        self.all_sprites = pygame.sprite.Group(self.defender, self.borders)

    def run(self) -> None:
        """Run the main game loop"""
        clock = pygame.time.Clock()

        while self.running:
            dt = clock.tick(Game.FPS) / 1000

            self.handle_events()
            self.update(dt)
            self.draw()

    def handle_events(self) -> None:
        """Run the event loops, running is False in case of termination request"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self, dt) -> None:
        self.defender.update(dt)
        if collisions := pygame.sprite.spritecollide(self.defender, self.borders, False):
            self.defender.bounce(collisions[0])

    def draw(self) -> None:
        self.screen.fill(Game.BACKGROUND_COLOR)
        self.all_sprites.draw(self.screen)
        self.window.flip()


if __name__ == "__main__":
    pygame.init()
    pg_window = pygame.Window(TITLE, WIN_SIZE, WIN_POS)
    pg_screen = pg_window.get_surface()

    Defender.load_resources()
    Border.load_resources()

    try:
        Game(pg_window, pg_screen).run()
    finally:
        pygame.quit()
        print("Done.")
