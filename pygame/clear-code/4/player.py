"""
Master Python by making 5 games - 4: Platformer

YouTube: https://www.youtube.com/watch?v=8OMghdHP-zs&t=26735s
GitHub: https://github.com/clear-code-projects/5games/tree/main/Platform
Google Drive: https://drive.google.com/drive/folders/1FCSPHzD9R4RBUypDTB_FIfwlyiCLA5WN

My version: https://github.com/egalli64/pythonesque/ pygame/clear-code folder
"""

import pygame
from sprite import AnimatedSprite
from bullet import Bullet, Fire
from timer import Timer  # type: ignore


class Player(AnimatedSprite):
    SPEED = 400
    GRAVITY = 50
    JUMP_SPEED = -20
    PATHNAME = "images/player"

    @classmethod
    def load_resources(cls):
        cls._frames = cls.import_folder(Player.PATHNAME)

    def __init__(self, pos, groups, obstacles):
        super().__init__(pos, Player._frames, groups)

        self.direction = pygame.Vector2()
        self.obstacles = obstacles
        self.on_floor = False
        self.flip = False

        self.cooldown = Timer(500)

    def set_horizontal_direction(self, x: int):
        self.direction.x = x

    def jump(self):
        if self.on_floor:
            self.direction.y = Player.JUMP_SPEED

    def shoot(self):
        if not self.cooldown:
            direction = -1 if self.flip else 1
            x = self.rect.centerx + direction * 34
            if self.flip:
                x -= Bullet._image.get_width()
            self.cooldown.activate()

            pos = (x, self.rect.centery)
            return Bullet(pos, direction), Fire(self.rect.center, self)
        else:
            return None

    def horizontal_collision(self):
        for obstacle in self.obstacles:
            if obstacle.rect.colliderect(self.rect):
                if self.direction.x > 0:
                    self.rect.right = obstacle.rect.left
                if self.direction.x < 0:
                    self.rect.left = obstacle.rect.right

    def vertical_collision(self):
        for obstacle in self.obstacles:
            if obstacle.rect.colliderect(self.rect):
                if self.direction.y > 0:
                    self.rect.bottom = obstacle.rect.top
                if self.direction.y < 0:
                    self.rect.top = obstacle.rect.bottom
                self.direction.y = 0

    def check_floor(self):
        probe = pygame.FRect((0, 0), (self.rect.width, 2)).move_to(
            midtop=self.rect.midbottom
        )
        self.on_floor = any(probe.colliderect(x.rect) for x in self.obstacles)

    def animate(self, dt):
        if self.direction.x:
            self.frame_index += Player.ANIMATION_SPEED * dt
            self.flip = self.direction.x < 0
        else:
            self.frame_index = 0

        if not self.on_floor:
            self.frame_index = 1

        self.image = self.frames[int(self.frame_index) % len(self.frames)]
        self.image = pygame.transform.flip(self.image, self.flip, False)

    def update(self, dt):
        self.check_floor()
        self.rect.x += self.direction.x * Player.SPEED * dt
        self.horizontal_collision()

        self.direction.y += Player.GRAVITY * dt
        self.rect.y += self.direction.y
        self.vertical_collision()

        self.cooldown.update()
        self.animate(dt)
