"""
Master Python by making 5 games - 4: Platformer

YouTube: https://www.youtube.com/watch?v=8OMghdHP-zs&t=26735s
GitHub: https://github.com/clear-code-projects/5games/tree/main/Platform
Google Drive: https://drive.google.com/drive/folders/1FCSPHzD9R4RBUypDTB_FIfwlyiCLA5WN

My version: https://github.com/egalli64/pythonesque/ pygame/clear-code folder
"""

import pygame
from pytmx.util_pygame import load_pygame
from camera import CameraGroup
from sprite import Sprite
from player import Player

WIN_RECT = pygame.Rect(0, 0, 1280, 720)
TITLE = "Platformer"


class Game:
    FPS = 60
    WORLD_FILENAME = "data/maps/world.tmx"
    TILE_SIZE = 64
    BACKGROUND_COLOR = "#fcdfcd"

    @classmethod
    def load_resources(cls):
        cls.tmx_map = load_pygame(cls.WORLD_FILENAME)

    def __init__(self, window, screen):
        self.window = window
        self.screen = screen
        self.clock = pygame.time.Clock()

        self.all_sprites = CameraGroup(WIN_RECT)
        self.obstacles = pygame.sprite.Group()

        for layer in Game.tmx_map.layers:
            match layer.name:
                case "Main":
                    for x, y, image in layer.tiles():
                        pos = (x * Game.TILE_SIZE, y * Game.TILE_SIZE)
                        Sprite(pos, image, (self.all_sprites, self.obstacles))
                case "Decoration":
                    for x, y, image in layer.tiles():
                        pos = (x * Game.TILE_SIZE, y * Game.TILE_SIZE)
                        Sprite(pos, image, self.all_sprites)
                case "Entities":
                    for obj in layer:
                        if obj.name == "Player":
                            pos = (obj.x, obj.y)
                            self.player = Player(pos, self.all_sprites, self.obstacles)

    def run(self):
        while self.handle_events():
            dt = self.clock.tick(Game.FPS) / 1000

            self.all_sprites.update(dt)

            self.screen.fill(Game.BACKGROUND_COLOR)
            self.all_sprites.camera_draw(screen, self.player.rect.center)
            window.flip()

    def handle_events(self) -> bool:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False

        keys = pygame.key.get_pressed()  # continuous events handling
        self.player.set_horizontal_direction(keys[pygame.K_RIGHT] - keys[pygame.K_LEFT])
        if keys[pygame.K_SPACE]:
            self.player.jump()

        return True


if __name__ == "__main__":
    pygame.init()
    window = pygame.Window(TITLE, WIN_RECT.size)
    screen = window.get_surface()

    Game.load_resources()
    Player.load_resources()

    try:
        Game(window, screen).run()
    finally:
        pygame.quit()
        print("Done.")
