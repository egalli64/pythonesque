"""
Master Python by making 5 games - 5: Monster battle

YouTube: https://www.youtube.com/watch?v=8OMghdHP-zs&t=32960s
GitHub: https://github.com/clear-code-projects/5games/tree/main/Monster%20battle
Google Drive: https://drive.google.com/drive/folders/15VQ37pgCwXxHZ8oBK0yc_CzKQeP2qSSl

My version: https://github.com/egalli64/pythonesque/ pygame/clear-code folder
"""

import pygame

from settings import WINDOW_HEIGHT, WINDOW_WIDTH, MONSTER_DATA
from support import folder_importer
from monster import Monster, Opponent
from random import choice


class Game:
    def __init__(self):
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Monster Battle")
        self.clock = pygame.time.Clock()
        self.running = True
        self.import_assets()

        # groups
        self.all_sprites = pygame.sprite.Group()

        # data
        player_monster_list = ["Sparchu", "Cleaf", "Jacana"]
        self.player_monsters = [
            Monster(name, self.back_surfs[name]) for name in player_monster_list
        ]
        self.monster = self.player_monsters[0]
        self.all_sprites.add(self.monster)
        opponent_name = choice(list(MONSTER_DATA.keys()))
        self.opponent = Opponent(
            opponent_name, self.front_surfs[opponent_name], self.all_sprites
        )

    def import_assets(self):
        self.back_surfs = folder_importer("images", "back")
        self.front_surfs = folder_importer("images", "front")
        self.bg_surfs = folder_importer("images", "other")

    def draw_monster_floor(self):
        for sprite in self.all_sprites:
            floor_rect = self.bg_surfs["floor"].get_frect(
                center=sprite.rect.midbottom + pygame.Vector2(0, -10)
            )
            self.display_surface.blit(self.bg_surfs["floor"], floor_rect)

    def run(self):
        while self.running:
            dt = self.clock.tick() / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False

            # update
            self.all_sprites.update(dt)

            # draw
            self.display_surface.blit(self.bg_surfs["bg"], (0, 0))
            self.draw_monster_floor()
            self.all_sprites.draw(self.display_surface)
            pygame.display.update()


if __name__ == "__main__":
    pygame.init()

    try:
        Game().run()
    finally:
        pygame.quit()
        print("Done.")
