"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Defender as a Sprite
"""
import pygame

FPS = 30
TITLE = "Defender as Sprite"
WIN_SIZE = (600, 100)
WIN_POS = (10, 50)
BACKGROUND_COLOR = "white"


class Defender(pygame.sprite.Sprite):
    FILENAME = "../images/defender.png"
    SIZE = (30, 30)
    X_VELOCITY = 150  # pixel/second
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
        mid_bottom = viewport.centerx, viewport.bottom - Defender.BOTTOM_GAP
        self.rect = pygame.FRect(self.image.get_rect(midbottom=mid_bottom))

        self.viewport = viewport
        self.x_velocity = Defender.X_VELOCITY

    def update(self, dt: float) -> None:
        self.rect.x += self.x_velocity * dt
        if self.rect.right >= self.viewport.right or self.rect.left <= self.viewport.left:
            self.rect.clamp_ip(self.viewport)
            self.x_velocity *= -1

    def draw(self, surface: pygame.Surface) -> None:
        surface.blit(self.image, self.rect)


def main(window: pygame.Window, screen: pygame.Surface) -> None:
    clock = pygame.time.Clock()
    defender = Defender(screen.get_rect())

    running = True
    while running:
        dt = clock.tick(FPS) / 1000
        running = handle_events()

        # Update
        defender.update(dt)

        # Draw
        screen.fill(BACKGROUND_COLOR)
        defender.draw(screen)
        window.flip()


def handle_events() -> bool:
    for event in pygame.event.get():
        match event.type:
            case pygame.QUIT:
                return False
            case pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False

    return True


if __name__ == "__main__":
    pygame.init()

    try:
        main_window = pygame.Window(TITLE, WIN_SIZE, WIN_POS)
        main_surface = main_window.get_surface()

        Defender.load_resources()

        main(main_window, main_surface)
    finally:
        pygame.quit()
