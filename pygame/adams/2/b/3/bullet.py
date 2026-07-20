"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Stereo sound
"""
from typing import override
import pygame
from tank import Tank
from direction import Direction


class Bullet(pygame.sprite.Sprite):
    SOUND_FILE = "../sounds/fire.wav"
    IMAGE_FILES = {
        Direction.LEFT: "../images/bullet_left.png",
        Direction.RIGHT: "../images/bullet_right.png",
    }
    TRANSPARENT_COLOR = "black"
    SPEED = 300

    image: pygame.Surface
    rect: pygame.FRect

    @classmethod
    def load_resources(cls) -> None:
        cls._sound = pygame.mixer.Sound(cls.SOUND_FILE)
        cls._images = {x: pygame.image.load(cls.IMAGE_FILES[x]).convert() for x in [Direction.LEFT, Direction.RIGHT]}

        for image in cls._images.values():
            image.set_colorkey(cls.TRANSPARENT_COLOR)

    def __init__(self, tank: Tank, viewport: pygame.Rect) -> None:
        assert tank.direction != Direction.UP, "Firing up is disabled"
        assert tank.direction != Direction.DOWN, "Firing down is disabled"
        super().__init__()

        self.image = Bullet._images[tank.direction]
        self.rect = pygame.FRect(self.image.get_rect())
        self.direction = tank.direction
        self.rect.center = tank.rect.center
        self.viewport = viewport

        if channel := pygame.mixer.find_channel():
            right = self.rect.centerx / self.viewport.width
            channel.set_volume(1 - right, right)
            channel.play(Bullet._sound)

    @override
    def update(self, dt) -> None:
        movement = pygame.Vector2(self.direction.value) * Bullet.SPEED * dt
        self.rect.move_ip(movement)
        if not self.viewport.contains(self.rect):
            self.kill()
