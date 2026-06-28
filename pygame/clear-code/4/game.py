"""
Master Python by making 5 games - 4: Platformer

YouTube: https://www.youtube.com/watch?v=8OMghdHP-zs&t=26735s
GitHub: https://github.com/clear-code-projects/5games/tree/main/Platform
Google Drive: https://drive.google.com/drive/folders/1FCSPHzD9R4RBUypDTB_FIfwlyiCLA5WN

My version: https://github.com/egalli64/pythonesque/ pygame/clear-code folder
"""

import pygame
from pytmx.util_pygame import load_pygame
from camera import Camera
from sprite import Sprite
from player import Player

WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
TILE_SIZE = 64
FPS = 60
BACKGROUND_COLOR = "#fcdfcd"


class Game:
    def __init__(self):
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Platformer")
        self.clock = pygame.time.Clock()
        self.running = True

        # groups
        self.all_sprites = Camera()
        self.collision_sprites = pygame.sprite.Group()

        # load game
        self.setup()

    def setup(self):
        tmx_map = load_pygame("data/maps/world.tmx")

        for x, y, image in tmx_map.get_layer_by_name("Main").tiles():  # type: ignore
            Sprite(
                (x * TILE_SIZE, y * TILE_SIZE),
                image,
                (self.all_sprites, self.collision_sprites),
            )

        for x, y, image in tmx_map.get_layer_by_name("Decoration").tiles():  # type: ignore
            Sprite((x * TILE_SIZE, y * TILE_SIZE), image, self.all_sprites)

        for obj in tmx_map.get_layer_by_name("Entities"):  # type: ignore
            if obj.name == "Player":
                self.player = Player(
                    (obj.x, obj.y), self.all_sprites, self.collision_sprites
                )

    def run(self):
        while self.running:
            dt = self.clock.tick(FPS) / 1000

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # update
            self.all_sprites.update(dt)

            # draw
            self.display_surface.fill(BACKGROUND_COLOR)
            self.all_sprites.camera_draw(self.player.rect.center)
            pygame.display.update()


if __name__ == "__main__":
    pygame.init()

    try:
        Game().run()
    finally:
        pygame.quit()
        print("Done.")
