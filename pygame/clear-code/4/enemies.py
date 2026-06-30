"""
Master Python by making 5 games - 4: Platformer

YouTube: https://www.youtube.com/watch?v=8OMghdHP-zs&t=26735s
GitHub: https://github.com/clear-code-projects/5games/tree/main/Platform
Google Drive: https://drive.google.com/drive/folders/1FCSPHzD9R4RBUypDTB_FIfwlyiCLA5WN

My version: https://github.com/egalli64/pythonesque/ pygame/clear-code folder
"""

from abc import ABC, abstractmethod
from math import sin
from random import randint
import pygame
from sprite import AnimatedSprite
from timer import Timer  # type: ignore


class Enemy(AnimatedSprite, ABC):
    SOUND_FILENAME = "audio/impact.ogg"

    @classmethod
    def load_resources(cls):
        cls.kill_sound = pygame.mixer.Sound(cls.SOUND_FILENAME)

    def __init__(self, frames, pos, groups):
        super().__init__(frames, pos, groups)
        self.death_timer = Timer(200, func=self.kill)

    def destroy(self):
        Enemy.kill_sound.play()
        self.death_timer.activate()
        self.animation_speed = 0
        self.image = pygame.mask.from_surface(self.image).to_surface()
        self.image.set_colorkey("black")

    def update(self, dt):
        self.death_timer.update()
        if not self.death_timer:
            self.move(dt)
            self.animate(dt)
        self.constraint()

    @abstractmethod
    def move(self, dt):
        pass

    @abstractmethod
    def constraint(self):
        pass


class Bee(Enemy):
    PATHNAME = "images/enemies/bee"
    SPEED_RANGE = (300, 500)
    AMPLITUDE_RANGE = (500, 600)
    FREQUENCY_RANGE = (300, 600)

    @classmethod
    def load_resources(cls):
        cls._frames = cls.import_folder(Bee.PATHNAME)

    def __init__(self, pos, groups):
        super().__init__(pos, Bee._frames, groups)
        self.speed = randint(*Bee.SPEED_RANGE)
        self.amplitude = randint(*Bee.AMPLITUDE_RANGE)
        self.frequency = randint(*Bee.FREQUENCY_RANGE)

    def move(self, dt):
        self.rect.x -= self.speed * dt
        angle = pygame.time.get_ticks() / self.frequency
        self.rect.y += sin(angle) * self.amplitude * dt

    def constraint(self):
        if self.rect.right <= 0:
            self.kill()


class Worm(Enemy):
    PATHNAME = "images/enemies/worm"
    SPEED_RANGE = (150, 200)

    @classmethod
    def load_resources(cls):
        cls._frames = cls.import_folder(Worm.PATHNAME)

    def __init__(self, rect, groups):
        super().__init__(rect.topleft, Worm._frames, groups)
        self.rect.bottomleft = rect.bottomleft
        self.main_rect = rect
        self.speed = randint(*Worm.SPEED_RANGE)
        self.direction = 1

    def move(self, dt):
        self.rect.x += self.direction * self.speed * dt

    def constraint(self):
        if not self.main_rect.contains(self.rect):
            self.direction *= -1
            self.frames = [
                pygame.transform.flip(surf, True, False) for surf in self.frames
            ]
