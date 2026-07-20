"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Stereo sound
"""
from typing import override
import pygame
from tank import Tank
from direction import Direction

TRANSPARENT_COLOR = "black"


class Bullet(pygame.sprite.Sprite):
    SOUND_FILE = "../sounds/fire.wav"
    IMAGE_FILES = {
        Direction.LEFT: "../images/bullet_left.png",
        Direction.RIGHT: "../images/bullet_right.png",
    }
    SPEED = 300

    image: pygame.Surface
    rect: pygame.Rect

    def __init__(self, tank: Tank, viewport: pygame.Rect) -> None:
        assert tank.direction != Direction.UP, "Firing up is disabled"
        assert tank.direction != Direction.DOWN, "Firing down is disabled"
        super().__init__()

        self.image = pygame.image.load(Bullet.IMAGE_FILES[tank.direction]).convert()
        self.image.set_colorkey(TRANSPARENT_COLOR)
        self.rect = self.image.get_rect()
        self.direction = tank.direction
        self.rect.center = tank.rect.center
        self.viewport = viewport

        self.channel = pygame.mixer.find_channel()
        if self.channel:
            sound = pygame.mixer.Sound(Bullet.SOUND_FILE)
            self.stereo()
            self.channel.play(sound)

    def stereo(self) -> None:
        right = self.rect.centerx / self.viewport.width
        self.channel.set_volume(1 - right, right)

    @override
    def update(self, dt) -> None:
        movement = pygame.Vector2(self.direction.value) * Bullet.SPEED * dt
        self.rect.move_ip(*movement)

        if not self.viewport.contains(self.rect):
            self.kill()
        else:
            self.stereo()
