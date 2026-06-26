"""
Master Python by making 5 games - 2: Vampire survivor

YouTube: https://www.youtube.com/watch?v=8OMghdHP-zs&t=13523s
GitHub: https://github.com/clear-code-projects/5games/tree/main/Vampire%20survivor
Google Drive: https://drive.google.com/drive/folders/1WBhwu1yAzgmNwQ2w-SI6G8hzqwQjUN-Z

My version: https://github.com/egalli64/pythonesque/ pygame/clear-code folder
"""

from os import walk
from os.path import join
from random import choice
import pygame


class Enemy(pygame.sprite.Sprite):
    PATHNAME = "images/enemies"
    SPEED = 250
    ANIMATION_SPEED = 6
    DEATH_DURATION = 0.4

    @classmethod
    def load_resources(cls):
        folders = list(walk(cls.PATHNAME))[0][1]
        cls._frames = {}
        for folder in folders:
            for folder_path, _, file_names in walk(join(cls.PATHNAME, folder)):
                for file_name in file_names:
                    full_path = join(folder_path, file_name)
                    image = pygame.image.load(full_path).convert_alpha()
                    cls._frames.setdefault(folder, []).append(image)

    def __init__(self, pos, player, obstacles):
        super().__init__()
        self.player = player
        self.obstacles = obstacles
        self.death_time = 0

        self.frames = choice(list(Enemy._frames.values()))
        self.frame_index = 0
        self.image = self.frames[self.frame_index]
        self.rect: pygame.FRect = self.image.get_frect(center=pos)
        self.hitbox_rect = self.rect.inflate(-20, -40)
        self.direction = pygame.Vector2()
        self.camera_layer = 1

    def animate(self, dt):
        self.frame_index += Enemy.ANIMATION_SPEED * dt
        self.image = self.frames[int(self.frame_index) % len(self.frames)]

    def move(self, dt):
        # get direction
        player_pos = pygame.Vector2(self.player.rect.center)
        enemy_pos = pygame.Vector2(self.rect.center)
        self.direction = (player_pos - enemy_pos).normalize()

        # update the rect position + collision
        self.hitbox_rect.x += self.direction.x * Enemy.SPEED * dt
        self.horizontal_collision()
        self.hitbox_rect.y += self.direction.y * Enemy.SPEED * dt
        self.vertical_collision()
        self.rect.center = self.hitbox_rect.center

    def horizontal_collision(self):
        for obstacle in self.obstacles:
            if obstacle.rect.colliderect(self.hitbox_rect):
                if self.direction.x > 0:
                    self.hitbox_rect.right = obstacle.rect.left
                if self.direction.x < 0:
                    self.hitbox_rect.left = obstacle.rect.right

    def vertical_collision(self):
        for obstacle in self.obstacles:
            if obstacle.rect.colliderect(self.hitbox_rect):
                if self.direction.y < 0:
                    self.hitbox_rect.top = obstacle.rect.bottom
                if self.direction.y > 0:
                    self.hitbox_rect.bottom = obstacle.rect.top

    def destroy(self):
        self.death_time = Enemy.DEATH_DURATION
        self.image = pygame.mask.from_surface(self.frames[0]).to_surface()
        self.image.set_colorkey("black")

    def update(self, dt):
        if self.death_time:
            self.death_time -= dt
            if self.death_time <= 0:
                self.kill()
        else:
            self.move(dt)
            self.animate(dt)
