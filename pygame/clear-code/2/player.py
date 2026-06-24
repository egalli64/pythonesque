"""
Master Python by making 5 games - 2: Vampire survivor

YouTube: https://www.youtube.com/watch?v=8OMghdHP-zs&t=13523s
GitHub: https://github.com/clear-code-projects/5games/tree/main/Vampire%20survivor
Google Drive: https://drive.google.com/drive/folders/1WBhwu1yAzgmNwQ2w-SI6G8hzqwQjUN-Z

My version: https://github.com/egalli64/pythonesque/ pygame/clear-code folder
"""

import pygame


class Player(pygame.sprite.Sprite):
    FILENAME = "images/player/down/0.png"
    SPEED = 500

    @classmethod
    def load_resources(cls):
        cls._image = pygame.image.load(Player.FILENAME).convert_alpha()

    def __init__(self, pos, obstacles):
        super().__init__()
        self.image = Player._image
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
        self.hitbox_rect.x += self.direction.x * self.speed * dt
        self.horizontal_collision()
        self.hitbox_rect.y += self.direction.y * self.speed * dt
        self.vertical_collision()
        self.rect.center = self.hitbox_rect.center
