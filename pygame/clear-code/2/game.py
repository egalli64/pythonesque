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
from pytmx.util_pygame import load_pygame

from player import Player
from tmx_objects import Ground, Collision
from camera import CameraGroup
from gun import Gun
from bullet import Bullet
from enemy import Enemy

WIN_RECT = pygame.Rect(0, 0, 1280, 720)
TITLE = "Vampire survivor"


class Game:
    FPS = 60
    BACKGROUND_COLOR = "black"
    FILENAME = "data/maps/world.tmx"
    TILE_SIZE = 64

    @classmethod
    def load_resources(cls):
        cls.tmx = load_pygame(cls.FILENAME)

    def __init__(self, window, screen):
        self.window = window
        self.screen = screen
        self.clock = pygame.time.Clock()

        self.obstacles = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()

        # camera - player - obstacles are intertwined, consider implementing a collision system
        pos = (WIN_RECT.centerx, WIN_RECT.centery - 30)
        self.player = Player(pos, self.obstacles)
        self.all_sprites = CameraGroup(WIN_RECT, self.player)
        self.all_sprites.add(self.player)

        self.gun = Gun(self.player, WIN_RECT.center, self.all_sprites)

        # enemies
        self.spawn_positions = []
        self.enemy_event = pygame.event.custom_type()
        pygame.time.set_timer(self.enemy_event, 300)

        folders = list(walk("images/enemies"))[0][1]
        self.enemy_frames = {}
        for folder in folders:
            for folder_path, _, file_names in walk(join("images/enemies", folder)):
                self.enemy_frames[folder] = []
                for file_name in sorted(
                    file_names, key=lambda name: int(name.split(".")[0])
                ):
                    full_path = join(folder_path, file_name)
                    surf = pygame.image.load(full_path).convert_alpha()
                    self.enemy_frames[folder].append(surf)

        for layer in Game.tmx.layers:
            match layer.name:
                case "Ground":
                    for x, y, image in layer.tiles():
                        pos = (x * Game.TILE_SIZE, y * Game.TILE_SIZE)
                        Ground(pos, image, self.all_sprites)
                case "Objects":
                    for obj in layer:
                        pos = (obj.x, obj.y)
                        Collision(pos, obj.image, (self.all_sprites, self.obstacles))
                case "Collisions":
                    for obj in layer:
                        image = pygame.Surface((obj.width, obj.height))
                        Collision((obj.x, obj.y), image, self.obstacles)
                case "Entities":
                    for obj in layer:
                        if obj.name == "Enemy":
                            self.spawn_positions.append((obj.x, obj.y))

    def run(self):
        while self.handle_events():
            dt = self.clock.tick(Game.FPS) / 1000

            self.all_sprites.update(dt)

            self.screen.fill(Game.BACKGROUND_COLOR)
            self.all_sprites.camera_draw(self.screen)
            window.flip()

    def handle_events(self) -> bool:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
            if event.type == self.enemy_event:
                Enemy(
                    choice(self.spawn_positions),
                    choice(list(self.enemy_frames.values())),
                    (self.all_sprites, self.enemies),
                    self.player,
                    self.obstacles,
                )

        keys = pygame.key.get_pressed()  # continuous events handling

        x = keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]
        y = keys[pygame.K_DOWN] - keys[pygame.K_UP]
        self.player.set_direction(x, y)

        if pygame.mouse.get_pressed()[0]:
            if bullet := self.gun.shoot():
                self.bullets.add(bullet)
                self.all_sprites.add(bullet)

        return True


if __name__ == "__main__":
    pygame.init()
    window = pygame.Window(TITLE, WIN_RECT.size)
    screen = window.get_surface()

    Game.load_resources()
    Player.load_resources()
    Gun.load_resources()
    Bullet.load_resources()

    try:
        Game(window, screen).run()
    finally:
        pygame.quit()
        print("Done.")
