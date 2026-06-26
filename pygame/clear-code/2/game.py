"""
Master Python by making 5 games - 2: Vampire survivor

YouTube: https://www.youtube.com/watch?v=8OMghdHP-zs&t=13523s
GitHub: https://github.com/clear-code-projects/5games/tree/main/Vampire%20survivor
Google Drive: https://drive.google.com/drive/folders/1WBhwu1yAzgmNwQ2w-SI6G8hzqwQjUN-Z

My version: https://github.com/egalli64/pythonesque/ pygame/clear-code folder
"""

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
    WORLD_FILENAME = "data/maps/world.tmx"
    MUSIC_FILENAME = "audio/music.wav"
    IMPACT_FILENAME = "audio/impact.ogg"
    TILE_SIZE = 64
    EVENT_CREATE_ENEMY = pygame.event.custom_type()
    DELTA_CREATE_ENEMY = 500

    @classmethod
    def load_resources(cls):
        cls.tmx = load_pygame(cls.WORLD_FILENAME)
        # cls.music = pygame.mixer.Sound(cls.MUSIC_FILENAME)
        # cls.music.set_volume(0.5)
        # cls.music.play(loops=-1)
        cls._impact = pygame.mixer.Sound(cls.IMPACT_FILENAME)

    def __init__(self, window, screen):
        self.window = window
        self.screen = screen
        self.clock = pygame.time.Clock()

        self.obstacles = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.enemies: pygame.sprite.Group[Enemy] = pygame.sprite.Group()
        self.all_sprites = CameraGroup(WIN_RECT, None)

        self.enemy_spawn_positions = []
        pygame.time.set_timer(Game.EVENT_CREATE_ENEMY, Game.DELTA_CREATE_ENEMY)

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
                        if obj.name == "Player":
                            self.player = Player((obj.x, obj.y), self.obstacles)
                            self.gun = Gun(self.player, WIN_RECT.center)
                            self.all_sprites.add((self.player, self.gun))
                            self.all_sprites.set_target(self.player)
                        if obj.name == "Enemy":
                            self.enemy_spawn_positions.append((obj.x, obj.y))

    def run(self):
        while self.handle_events():
            dt = self.clock.tick(Game.FPS) / 1000

            self.bullet_collisions()
            if self.enemy_collision():
                break
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
            if event.type == Game.EVENT_CREATE_ENEMY:
                pos = choice(self.enemy_spawn_positions)
                enemy = Enemy(pos, self.player, self.obstacles)
                self.all_sprites.add(enemy)
                self.enemies.add(enemy)

        keys = pygame.key.get_pressed()  # continuous events handling

        x = keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]
        y = keys[pygame.K_DOWN] - keys[pygame.K_UP]
        self.player.set_direction(x, y)

        if pygame.mouse.get_pressed()[0]:
            if bullet := self.gun.shoot():
                self.bullets.add(bullet)
                self.all_sprites.add(bullet)

        return True

    def bullet_collisions(self):
        for bullet in self.bullets:
            enemies = pygame.sprite.spritecollide(bullet, self.enemies, False)
            if enemies:
                self._impact.play()
                for enemy in enemies:
                    enemy.destroy()
                bullet.kill()

    def enemy_collision(self):
        collided = lambda a, b: pygame.sprite.collide_mask(a, b) is not None
        return pygame.sprite.spritecollideany(self.player, self.enemies, collided)


if __name__ == "__main__":
    pygame.init()
    window = pygame.Window(TITLE, WIN_RECT.size)
    screen = window.get_surface()

    Game.load_resources()
    Player.load_resources()
    Gun.load_resources()
    Bullet.load_resources()
    Enemy.load_resources()

    try:
        Game(window, screen).run()
    finally:
        pygame.time.wait(1000)
        pygame.quit()
        print("Done.")
