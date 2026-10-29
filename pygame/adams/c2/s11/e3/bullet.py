"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Stereo sound
"""
from typing import override
import pygame
from direction import Direction

SOUND_FILE = "../sounds/fire.wav"
IMAGE_FILES = {
    Direction.LEFT: "../images/bullet_left.png",
    Direction.RIGHT: "../images/bullet_right.png",
}
TRANSPARENT_COLOR = "black"
SPEED = 300


class Bullet(pygame.sprite.Sprite):
    image: pygame.Surface
    _images: dict[Direction, pygame.Surface]
    rect: pygame.FRect
    direction: Direction

    @classmethod
    def load_resources(cls) -> None:
        cls._sound = pygame.mixer.Sound(SOUND_FILE)

        cls._images = {}
        for direction, path in IMAGE_FILES.items():
            image = pygame.image.load(path).convert()
            image.set_colorkey(TRANSPARENT_COLOR)
            cls._images[direction] = image

    def __init__(self, viewport: pygame.Rect, origin: tuple[float, float], direction: Direction) -> None:
        assert direction != Direction.UP, "Firing up is disabled"
        assert direction != Direction.DOWN, "Firing down is disabled"
        super().__init__()

        self.image = Bullet._images[direction]
        self.rect = pygame.FRect(self.image.get_rect(center=origin))
        self.direction = direction
        self.viewport = viewport

        if channel := pygame.mixer.find_channel():
            right = self.rect.centerx / self.viewport.width
            channel.set_volume(1 - right, right)
            channel.play(Bullet._sound)

    @override
    def update(self, dt: float) -> None:
        movement = pygame.Vector2(self.direction.value) * SPEED * dt
        self.rect.move_ip(movement)

        if not self.viewport.colliderect(self.rect):
            self.kill()
