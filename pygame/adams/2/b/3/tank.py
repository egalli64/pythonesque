"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Stereo sound
"""
from typing import override
import pygame
from direction import Direction

TILE_SIZE = 32  # square tile, in bit
TRANSPARENT_COLOR = "black"

class Tank(pygame.sprite.Sprite):
    IMAGE = "../images/tank.png"
    SOUND = "../sounds/drive.wav"
    SPEED = 50

    image: pygame.Surface
    rect: pygame.FRect

    def __init__(self, viewport: pygame.Rect) -> None:
        super().__init__()
        self.viewport = viewport
        self.images = {}

        picture = pygame.image.load(Tank.IMAGE).convert()
        picture.set_colorkey(TRANSPARENT_COLOR)
        self.images[Direction.UP] = picture
        self.images[Direction.LEFT] = pygame.transform.rotate(picture, 90)
        self.images[Direction.RIGHT] = pygame.transform.rotate(picture, -90)
        self.images[Direction.DOWN] = pygame.transform.rotate(picture, 180)

        self.direction = Direction.RIGHT
        self.image = self.images[self.direction]
        self.rect = pygame.FRect(self.image.get_rect())
        assert self.rect.width == self.rect.height == TILE_SIZE, "Bad tile size"

        self.rect.left, self.rect.top = 3 * TILE_SIZE, 2 * TILE_SIZE  # initial position
        self.channel = pygame.mixer.find_channel()
        if self.channel:
            sound = pygame.mixer.Sound(Tank.SOUND)
            self.stereo()
            self.channel.play(sound, -1)
        self.speed = None

    @override
    def update(self, dt: float) -> None:
        self.image = self.images[self.direction]
        movement = pygame.Vector2(self.direction.value) * Tank.SPEED * dt
        self.rect.move_ip(movement)

        if not self.viewport.contains(self.rect):
            self.direction = self.direction.opposite

        self.stereo()

    def stereo(self) -> None:
        right = self.rect.centerx / self.viewport.width
        self.channel.set_volume(1 - right, right)

    def turn(self, direction: Direction) -> None:
        self.direction = direction

