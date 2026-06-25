"""
Master Python by making 5 games - 2: Vampire survivor

YouTube: https://www.youtube.com/watch?v=8OMghdHP-zs&t=13523s
GitHub: https://github.com/clear-code-projects/5games/tree/main/Vampire%20survivor
Google Drive: https://drive.google.com/drive/folders/1WBhwu1yAzgmNwQ2w-SI6G8hzqwQjUN-Z

My version: https://github.com/egalli64/pythonesque/ pygame/clear-code folder
"""

import pygame
from pytmx.util_pygame import load_pygame
from player import Player
from tmx_objects import Ground, Collision
from camera import CameraGroup
from gun import Gun
from bullet import Bullet

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

        # camera - player - obstacles are intertwined, consider implementing a collision system
        pos = (WIN_RECT.centerx, WIN_RECT.centery - 30)
        self.player = Player(pos, self.obstacles)
        self.all_sprites = CameraGroup(WIN_RECT, self.player)
        self.all_sprites.add(self.player)

        for layer in Game.tmx.layers:
            if layer.name == "Ground":
                for x, y, image in layer.tiles():
                    pos = (x * Game.TILE_SIZE, y * Game.TILE_SIZE)
                    Ground(pos, image, self.all_sprites)
            if layer.name == "Objects":
                for obj in layer:
                    pos = (obj.x, obj.y)
                    Collision(pos, obj.image, (self.all_sprites, self.obstacles))
            if layer.name == "Collisions":
                for obj in layer:
                    image = pygame.Surface((obj.width, obj.height))
                    Collision((obj.x, obj.y), image, self.obstacles)

        self.gun = Gun(self.player, WIN_RECT.center, self.all_sprites)

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
