"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Mouse actions
"""
import pygame


class Ball(pygame.sprite.Sprite):
    FILENAME = "../../images/blue_ball.png"
    MIN_SIZE = 10
    INITIAL_SIZE_RATIO = 5

    image: pygame.Surface
    scaled_image: pygame.Surface
    rect: pygame.FRect
    dirty: bool

    @classmethod
    def load_resources(cls) -> None:
        cls._image = pygame.image.load(cls.FILENAME).convert_alpha()

    def __init__(self, viewport: pygame.Rect) -> None:
        super().__init__()

        self.viewport = viewport
        self.max_size = min(viewport.width, viewport.height)
        self.size = self.max_size // Ball.INITIAL_SIZE_RATIO
        self.angle = 0

        self.rebuild()
        self.rect.center = viewport.center

    def rebuild(self):
        self.update_scaled_image()
        self.update_image()

    def update_scaled_image(self) -> None:
        self.scaled_image = pygame.transform.scale(Ball._image, (self.size, self.size))
        self.rect = pygame.FRect(self.scaled_image.get_rect())
        self.rect.clamp_ip(self.viewport)

    def update_image(self) -> None:
        self.image = pygame.transform.rotate(self.scaled_image, self.angle)

    def move(self, pos: tuple[int, int]) -> None:
        if self.rect.center != pos:
            self.rect.center = pos
            self.rect.clamp_ip(self.viewport)

    def rotate(self, counterclockwise: bool) -> None:
        self.angle = (self.angle + (90 if counterclockwise else -90)) % 360
        self.update_image()

    def resize(self, delta: int) -> None:
        candidate = self.size + delta
        if Ball.MIN_SIZE <= candidate <= self.max_size:
            self.size = candidate
            self.rebuild()
