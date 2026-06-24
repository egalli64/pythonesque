"""
Master Python by making 5 games - 2: Vampire survivor

YouTube: https://www.youtube.com/watch?v=8OMghdHP-zs&t=13523s
GitHub: https://github.com/clear-code-projects/5games/tree/main/Vampire%20survivor
Google Drive: https://drive.google.com/drive/folders/1WBhwu1yAzgmNwQ2w-SI6G8hzqwQjUN-Z

My version: https://github.com/egalli64/pythonesque/ pygame/clear-code folder
"""

from enum import Enum, auto
from os import walk
from os.path import join

import pygame


class Direction(Enum):
    LEFT = auto()
    RIGHT = auto()
    UP = auto()
    DOWN = auto()

    def __str__(self) -> str:
        return self.name.lower()


class Player(pygame.sprite.Sprite):
    PATHNAME = "images/player"
    SPEED = 500
    ANIMATION_SPEED = 10

    @classmethod
    def load_resources(cls):
        cls._frames = {}
        for direction in Direction:
            for folder_path, _, file_names in walk(join(cls.PATHNAME, str(direction))):
                for file_name in file_names:
                    full_path = join(folder_path, file_name)
                    image = pygame.image.load(full_path).convert_alpha()
                    cls._frames.setdefault(direction, []).append(image)

    def __init__(self, pos, obstacles):
        super().__init__()
        self.state: Direction = Direction.DOWN
        self.frame_index = 0
        self.image = Player._frames[self.state][self.frame_index]
        self.rect: pygame.FRect = self.image.get_frect(center=pos)

        self.direction = pygame.Vector2()
        self.speed = Player.SPEED
        self.obstacles = obstacles
        self.hitbox_rect = self.rect.inflate(-60, -90)
        self.camera_layer = 1

    def set_direction(self, x: int, y: int):
        self.direction.update(x, y)
        if self.direction:
            self.direction.normalize_ip()

        if self.direction.y != 0:
            self.state = Direction.DOWN if self.direction.y > 0 else Direction.UP
        elif self.direction.x != 0:
            self.state = Direction.RIGHT if self.direction.x > 0 else Direction.LEFT

    def horizontal_collision(self):
        for obstacle in self.obstacles:
            if obstacle.rect.colliderect(self.hitbox_rect):
                if self.direction.x > 0:
                    self.hitbox_rect.right = obstacle.rect.left
                elif self.direction.x < 0:
                    self.hitbox_rect.left = obstacle.rect.right

    def vertical_collision(self):
        for obstacle in self.obstacles:
            if obstacle.rect.colliderect(self.hitbox_rect):
                if self.direction.y < 0:
                    self.hitbox_rect.top = obstacle.rect.bottom
                elif self.direction.y > 0:
                    self.hitbox_rect.bottom = obstacle.rect.top

    def update(self, dt):
        # move
        self.hitbox_rect.x += self.direction.x * self.speed * dt
        self.horizontal_collision()
        self.hitbox_rect.y += self.direction.y * self.speed * dt
        self.vertical_collision()
        self.rect.center = self.hitbox_rect.center

        # choose image
        self.frame_index = self.frame_index + 5 * dt if self.direction else 0
        i = int(self.frame_index) % len(self._frames[self.state])
        self.image = self._frames[self.state][i]
