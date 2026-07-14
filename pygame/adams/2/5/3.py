"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Sprite Group
"""
import pygame

FPS = 30

TITLE = "Sprite Group"
WIN_SIZE = (600, 100)
WIN_POS = (10, 50)
BACKGROUND_COLOR = "white"


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
        self.rect = pygame.FRect(self.image.get_rect())
        self.rect.midbottom = viewport.centerx, viewport.bottom - Defender.BOTTOM_GAP
        self.x_velocity = Defender.X_SPEED

    def update(self, dt: float) -> None:
        self.rect.move_ip(self.x_velocity * dt, 0)

    def bounce(self, border: Border) -> None:
        if border.right:
            self.rect.right = border.rect.left
            self.x_velocity = -Defender.X_SPEED
        else:
            self.rect.left = border.rect.right
            self.x_velocity = Defender.X_SPEED


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


def main(window: pygame.Window, screen: pygame.Surface) -> None:
    clock = pygame.time.Clock()
    viewport = screen.get_rect()

    defender = Defender(viewport)
    all_sprites = pygame.sprite.Group(defender)
    borders: pygame.sprite.Group[Border] = pygame.sprite.Group(Border(viewport), Border(viewport, right=True))
    all_sprites.add(borders)

    running = True
    while running:
        dt = clock.tick(FPS) / 1000

        running = handle_events()

        # Update
        defender.update(dt)
        # here no more than one collision is expected
        if collisions := pygame.sprite.spritecollide(defender, borders, False):
            defender.bounce(collisions[0])

        # Draw
        screen.fill(BACKGROUND_COLOR)
        all_sprites.draw(screen)  # the group knows how to draw its sprites
        window.flip()


# noinspection DuplicatedCode
def handle_events() -> bool:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True


if __name__ == "__main__":
    pygame.init()
    pg_window = pygame.Window(TITLE, WIN_SIZE, WIN_POS)
    pg_screen = pg_window.get_surface()

    Defender.load_resources()
    Border.load_resources()

    try:
        main(pg_window, pg_screen)
    finally:
        pygame.quit()
        print("Done.")
