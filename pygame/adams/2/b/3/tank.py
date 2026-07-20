"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Stereo sound
"""
from typing import override
import pygame
from direction import Direction

TILE_SIZE = 32  # square tile, in bit


class Tank(pygame.sprite.Sprite):
    IMAGE_FILE = "../images/tank.png"
    TRANSPARENT_COLOR = "black"
    SOUND_FILE = "../sounds/drive.wav"
    SPEED = 50

    image: pygame.Surface
    rect: pygame.FRect

    @classmethod
    def load_resources(cls) -> None:
        cls._sound = pygame.mixer.Sound(cls.SOUND_FILE)

        image = pygame.image.load(cls.IMAGE_FILE).convert()
        image.set_colorkey(cls.TRANSPARENT_COLOR)
        cls._images = {
            Direction.UP: image,
            Direction.LEFT: pygame.transform.rotate(image, 90),
            Direction.RIGHT: pygame.transform.rotate(image, -90),
            Direction.DOWN: pygame.transform.rotate(image, 180)
        }

    def __init__(self, viewport: pygame.Rect) -> None:
        super().__init__()

        self.viewport = viewport
        self.direction = Direction.RIGHT
        self.image = self._images[self.direction]
        self.rect = pygame.FRect(self.image.get_rect())

        assert self.rect.width == self.rect.height == TILE_SIZE, "Bad tile size"
        self.rect.left, self.rect.top = 3 * TILE_SIZE, 2 * TILE_SIZE  # initial position
        self.channel = pygame.mixer.find_channel()
        if self.channel:
            self.stereo()
            self.channel.play(Tank._sound, -1)

    @override
    def update(self, dt: float) -> None:
        movement = pygame.Vector2(self.direction.value) * Tank.SPEED * dt
        self.rect.move_ip(movement)

        if not self.viewport.contains(self.rect):
            self.direction = self.direction.opposite
            self.image = self._images[self.direction]

        self.stereo()

    def stereo(self) -> None:
        if self.direction in (Direction.LEFT, Direction.RIGHT):
            right = self.rect.centerx / self.viewport.width
            self.channel.set_volume(1 - right, right)

    def turn(self, direction: Direction) -> None:
        if direction != self.direction:
            self.direction = direction
            self.image = self._images[self.direction]
