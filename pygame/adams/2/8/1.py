"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Types of collision
"""

from os import path
from typing import Any
import pygame

FPS = 30

WIN_RECT = pygame.Rect(0, 0, 700, 200)
TITLE = "Collision Types"


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, filename1: str, filename2: str) -> None:
        super().__init__()
        self.image_normal = pygame.image.load(filename1).convert_alpha()
        self.image_hit = pygame.image.load(filename2).convert_alpha()
        self.image = self.image_normal
        self.rect: pygame.Rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.radius = self.rect.centerx
        self.rect.centery = WIN_RECT.centery
        self.hit = False

    def update(self, *args: Any, **kwargs: Any) -> None:
        if "hit" in kwargs.keys():
            self.hit = kwargs["hit"]
        self.image = self.image_hit if (self.hit) else self.image_normal


class Bullet(pygame.sprite.Sprite):

    def __init__(self, picturefile: str) -> None:
        super().__init__()
        self.image = pygame.image.load(picturefile).convert_alpha()
        self.rect: pygame.Rect = self.image.get_rect()
        self.radius = self.rect.centery
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.center = (10, 10)
        self.directions = {
            "stop": (0, 0),
            "down": (0, 1),
            "up": (0, -1),
            "left": (-1, 0),
            "right": (1, 0),
        }
        self.set_direction("stop")

    def update(self, *args: Any, **kwargs: Any) -> None:
        if "action" in kwargs.keys():
            if kwargs["action"] == "move":
                self.rect.move_ip(self.speed)
        elif "direction" in kwargs.keys():
            self.set_direction(kwargs["direction"])

    def set_direction(self, direction: str) -> None:
        self.speed = self.directions[direction]


class Game(object):
    BULLET = "images/shoot.png"
    BRICK = ("images/brick1.png", "images/brick2.png")
    SHIP = ("images/ship1.png", "images/ship2.png")
    ALIEN = ("images/alienbig1.png", "images/alienbig2.png")
    DEFAULT_MODE = "rect"

    def __init__(self) -> None:
        self.window = pygame.Window(TITLE, WIN_RECT.size)
        self.screen = self.window.get_surface()
        self.clock = pygame.time.Clock()

        self.font = pygame.font.Font(None, 24)
        self.bullet = Bullet(Game.BULLET)
        self.bullet_group = pygame.sprite.GroupSingle(self.bullet)
        self.all_obstacles = pygame.sprite.Group()
        self.all_obstacles.add(Obstacle(*Game.BRICK))
        self.all_obstacles.add(Obstacle(*Game.SHIP))
        self.all_obstacles.add(Obstacle(*Game.ALIEN))
        self.mode = Game.DEFAULT_MODE
        self.running = False

    def run(self) -> None:
        self.resize()
        self.running = True
        while self.running:
            self.watch_for_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        pygame.quit()

    def watch_for_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                elif event.key == pygame.K_DOWN:
                    self.bullet.update(direction="down")
                elif event.key == pygame.K_UP:
                    self.bullet.update(direction="up")
                elif event.key == pygame.K_LEFT:
                    self.bullet.update(direction="left")
                elif event.key == pygame.K_RIGHT:
                    self.bullet.update(direction="right")
                elif event.key == pygame.K_r:
                    self.mode = "rect"
                elif event.key == pygame.K_c:
                    self.mode = "circle"
                elif event.key == pygame.K_m:
                    self.mode = "mask"
            elif event.type == pygame.KEYUP:
                self.bullet.update(direction="stop")

    def update(self) -> None:
        self.check_for_collision()
        self.bullet_group.update(action="move")
        self.all_obstacles.update()

    def draw(self) -> None:
        self.screen.fill("white")
        self.all_obstacles.draw(self.screen)
        self.bullet_group.draw(self.screen)
        text_surface_modus = self.font.render(f"Mode: {self.mode}", True, "blue")
        self.screen.blit(text_surface_modus, dest=(10, WIN_RECT.bottom - 30))
        self.window.flip()

    def resize(self) -> None:
        total_width = 0
        for s in self.all_obstacles:
            total_width += s.rect.width
        padding = (WIN_RECT.width - total_width) // 4
        for i in range(len(self.all_obstacles)):
            if i == 0:
                self.all_obstacles.sprites()[i].rect.left = padding
            else:
                self.all_obstacles.sprites()[i].rect.left = (
                    self.all_obstacles.sprites()[i - 1].rect.right + padding
                )

    def check_for_collision(self) -> None:
        if self.mode == "circle":
            for s in self.all_obstacles:
                s.update(hit=pygame.sprite.collide_circle(self.bullet, s))
        elif self.mode == "mask":
            for s in self.all_obstacles:
                s.update(hit=pygame.sprite.collide_mask(self.bullet, s))
        else:
            for s in self.all_obstacles:
                s.update(hit=pygame.sprite.collide_rect(self.bullet, s))


if __name__ == "__main__":
    pygame.init()

    try:
        Game().run()
    finally:
        pygame.quit()
        print("Done.")
