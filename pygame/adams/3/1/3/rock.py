"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Colliding rocks
"""
import random
import pygame
from animation import Animation


class Rock(pygame.sprite.Sprite):
    FILENAME = "../images/rock.png"
    EXPLOSION_TEMPLATE = "../images/explosion-{:d}.png"

    def __init__(self, viewport: pygame.Rect):
        super().__init__()
        self.image: pygame.Surface = pygame.image.load(Rock.FILENAME).convert_alpha()
        self.rect: pygame.FRect = pygame.FRect(self.image.get_rect())
        self.viewport = viewport

        max_pos = (self.rect.width * 2, viewport.height - self.rect.height)
        self.rect.centerx = random.randint(int(self.rect.width), int(max_pos[0]))
        self.rect.centery = random.randint(int(self.rect.height), int(max_pos[1]))

        speed_x = random.randint(-100, 100)
        speed_y = random.randint(-100, 100)
        self.speed = pygame.math.Vector2(speed_x, speed_y)

        explosions = [Rock.EXPLOSION_TEMPLATE.format(i) for i in range(1, 5)]
        self.animation = Animation(explosions, 100)
        self.explosion = False

    def update(self, dt) -> None:
        if self.explosion:
            self.image = self.animation.current()
            center = self.rect.center
            self.rect = pygame.FRect(self.image.get_rect())
            self.rect.center = center
        else:
            self.rect.move_ip(self.speed * dt)
            if self.rect.top <= 0 or self.rect.bottom >= self.viewport.height:
                self.speed.y *= -1
            if self.rect.left <= 0 or self.rect.right >= self.viewport.width:
                self.speed.x *= -1
        if self.animation.done():
            self.kill()

    def explode(self):
        self.explosion = True
