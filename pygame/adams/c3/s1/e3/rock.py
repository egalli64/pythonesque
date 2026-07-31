"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Colliding rocks
"""
import random
import pygame
from explosion import Explosion


class Rock(pygame.sprite.Sprite):
    FILENAME = "../../images/rock.png"
    LIFE_SPAN_INTERVAL = (100, 2000)
    SPEED_INTERVAL = (-100, 100)

    @classmethod
    def load_resources(cls) -> None:
        cls._image = pygame.image.load(Rock.FILENAME).convert_alpha()

    image: pygame.Surface
    rect: pygame.FRect

    def __init__(self, viewport: pygame.Rect):
        super().__init__()

        self.image = Rock._image
        self.viewport = viewport
        width, height = self.image.get_size()
        bottom_right = (random.randint(width, viewport.width), random.randint(height, viewport.height))
        self.rect = pygame.FRect(self.image.get_rect(bottomright=bottom_right))

        speed_x = random.randint(*Rock.SPEED_INTERVAL)
        speed_y = random.randint(*Rock.SPEED_INTERVAL)
        self.speed = pygame.math.Vector2(speed_x, speed_y)

        self.animation = Explosion()
        self.explosion = False

    def update(self, dt) -> None:
        if self.explosion:
            if self.animation.done():
                self.kill()
            else:
                self.image = self.animation.current()
                self.rect = pygame.FRect(self.image.get_rect(center=self.rect.center))
        else:
            self.rect.move_ip(self.speed * dt)
            self.rect.clamp_ip(self.viewport)
            if self.rect.top == 0 or self.rect.bottom == self.viewport.height:
                self.speed.y *= -1
            if self.rect.left == 0 or self.rect.right == self.viewport.width:
                self.speed.x *= -1

    def explode(self):
        self.explosion = True
