"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Stereo sound
"""
from typing import override
import pygame
from tank import Tank

FPS = 30
TITLE = "Stereo panning sound"
TILE_SIZE = 32  # square tile, in bit
MAP_SIZE = (25, 7)  # tiles, width, height
WIN_SIZE = (TILE_SIZE * MAP_SIZE[0], TILE_SIZE * MAP_SIZE[1])
TRANSPARENT_COLOR = "black"


class Bullet(pygame.sprite.Sprite):
    SOUND = "sounds/fire.wav"
    IMAGES = {
        Tank.Direction.LEFT: "images/bullet_left.png",
        Tank.Direction.RIGHT: "images/bullet_right.png",
    }
    SPEED = 300

    image: pygame.Surface
    rect: pygame.Rect

    def __init__(self, tank: Tank, viewport: pygame.Rect) -> None:
        assert tank.direction != Tank.Direction.UP, "Firing up is disabled"
        assert tank.direction != Tank.Direction.DOWN, "Firing down is disabled"
        super().__init__()

        self.image = pygame.image.load(Bullet.IMAGES[tank.direction]).convert()
        self.image.set_colorkey(TRANSPARENT_COLOR)
        self.rect = self.image.get_rect()
        self.direction = tank.direction
        self.rect.center = tank.rect.center
        self.viewport = viewport

        self.channel = pygame.mixer.find_channel()
        if self.channel:
            sound = pygame.mixer.Sound(Bullet.SOUND)
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
