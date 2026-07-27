"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Stereo sound
"""
from typing import override
import pygame
from ground import Ground
from bullet import Bullet
from direction import Direction


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
        top_left = 3 * Ground.TILE_SIZE[0], 2 * Ground.TILE_SIZE[1]
        self.rect = pygame.FRect(self.image.get_rect(topleft=top_left))

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

    def fire(self, burst_size: int) -> Bullet | None:
        if burst_size > 4 or self.direction in [Direction.UP, Direction.DOWN]:
            print("Fire disabled!")
            return None
        else:
            return Bullet(self.viewport, self.rect.center, self.direction)
