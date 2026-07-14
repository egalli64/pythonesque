"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Sprite collision
"""
import pygame

FPS = 30

TITLE = "Sprite collision"
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

    def draw(self, surface: pygame.Surface) -> None:
        surface.blit(self.image, self.rect)

    def bounce_right(self, border: Border) -> None:
        self.rect.left = border.rect.right
        self.x_velocity = Defender.X_SPEED

    def bounce_left(self, border: Border) -> None:
        self.rect.right = border.rect.left
        self.x_velocity = -Defender.X_SPEED


class Border(pygame.sprite.Sprite):
    FILENAME = "../images/brick.png"
    SIZE = (35, WIN_SIZE[1])

    @classmethod
    def load_resources(cls):
        image = pygame.image.load(cls.FILENAME).convert_alpha()
        cls._image = pygame.transform.scale(image, cls.SIZE)

    rect: pygame.Rect
    image: pygame.Surface

    def __init__(self, viewport: pygame.Rect, right: bool = False) -> None:
        super().__init__()

        self.image = Border._image
        self.rect = self.image.get_rect()
        if right:
            self.rect.right = viewport.right
        else:
            self.rect.left = viewport.left

    def draw(self, screen: pygame.Surface) -> None:
        screen.blit(self.image, self.rect)


def main(window: pygame.Window, screen: pygame.Surface) -> None:
    clock = pygame.time.Clock()
    viewport = screen.get_rect()

    defender = Defender(viewport)
    border_left = Border(viewport)
    border_right = Border(viewport, right=True)

    running = True
    while running:
        dt = clock.tick(FPS) / 1000

        running = handle_events()

        # Update
        defender.update(dt)

        if pygame.sprite.collide_rect(defender, border_left):
            defender.bounce_right(border_left)
        elif pygame.sprite.collide_rect(defender, border_right):
            defender.bounce_left(border_right)

        # Draw
        screen.fill(BACKGROUND_COLOR)
        defender.draw(screen)
        border_left.draw(screen)
        border_right.draw(screen)

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
