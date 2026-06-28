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
TILE_SIZE = 64
FPS = 60
BACKGROUND_COLOR = "#fcdfcd"


class Game:
    def __init__(self, window, screen):
        self.window = window
        self.screen = screen
        self.clock = pygame.time.Clock()

        self.all_sprites = CameraGroup(WIN_RECT)
        self.collision_sprites = pygame.sprite.Group()

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
        while self.handle_events():
            dt = self.clock.tick(FPS) / 1000

            self.all_sprites.update(dt)

            self.screen.fill(BACKGROUND_COLOR)
            self.all_sprites.camera_draw(screen, self.player.rect.center)
            window.flip()

    def handle_events(self) -> bool:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
        return True


if __name__ == "__main__":
    pygame.init()
    window = pygame.Window(TITLE, WIN_RECT.size)
    screen = window.get_surface()

    try:
        Game(window, screen).run()
    finally:
        pygame.quit()
        print("Done.")
