"""
Master Python by making 5 games - 5: Monster battle

YouTube: https://www.youtube.com/watch?v=8OMghdHP-zs&t=32960s
GitHub: https://github.com/clear-code-projects/5games/tree/main/Monster%20battle
Google Drive: https://drive.google.com/drive/folders/15VQ37pgCwXxHZ8oBK0yc_CzKQeP2qSSl

My version: https://github.com/egalli64/pythonesque/ pygame/clear-code folder
"""

import pygame

WIN_RECT = pygame.Rect(0, 0, 1280, 720)
TITLE = "Monster Battle"


from settings import MONSTER_DATA, ABILITIES_DATA, ELEMENT_DATA
from support import folder_importer
from monster import Monster, Opponent
from random import choice
from ui import UI
from timer import Timer  # type: ignore


class Game:
    FPS = 60

    def __init__(self, window, screen):
        self.window = window
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.import_assets()
        self.player_active = True

        # groups
        self.all_sprites = pygame.sprite.Group()

        # data
        player_monster_list = [
            "Sparchu",
            "Cleaf",
            "Jacana",
            "Gulfin",
            "Pouch",
            "Larvea",
        ]
        self.player_monsters = [
            Monster(name, self.back_surfs[name]) for name in player_monster_list
        ]
        self.monster = self.player_monsters[0]
        self.all_sprites.add(self.monster)
        opponent_name = choice(list(MONSTER_DATA.keys()))
        self.opponent = Opponent(
            opponent_name, self.front_surfs[opponent_name], self.all_sprites
        )

        # ui
        self.ui = UI(
            self.screen,
            self.monster,
            self.player_monsters,
            self.simple_surfs,
            self.get_input,
        )

        # timers
        self.timers = {
            "player end": Timer(1000, func=self.opponent_turn),
            "opponent end": Timer(1000, func=self.player_turn),
        }

    def get_input(self, state, data=None):
        if state == "attack":
            self.apply_attack(self.opponent, data)

        elif state == "escape":
            self.running = False
        self.player_active = False
        self.timers["player end"].activate()

    def apply_attack(self, target, attack):
        attack_data = ABILITIES_DATA[attack]
        attack_multiplier = ELEMENT_DATA[attack_data["element"]][target.element]
        target.health -= attack_data["damage"] * attack_multiplier
        print(f"{attack},{target.health}/{target.max_health}")

    def opponent_turn(self):
        attack = choice(self.opponent.abilities)
        self.apply_attack(self.monster, attack)
        self.timers["opponent end"].activate()

    def player_turn(self):
        self.player_active = True

    def update_timers(self):
        for timer in self.timers.values():
            timer.update()

    def import_assets(self):
        self.back_surfs = folder_importer("images", "back")
        self.front_surfs = folder_importer("images", "front")
        self.bg_surfs = folder_importer("images", "other")
        self.simple_surfs = folder_importer("images", "simple")

    def draw_monster_floor(self):
        for sprite in self.all_sprites:
            floor_rect = self.bg_surfs["floor"].get_frect(
                center=sprite.rect.midbottom + pygame.Vector2(0, -10)
            )
            self.screen.blit(self.bg_surfs["floor"], floor_rect)

    def run(self):
        while self.handle_events():
            dt = self.clock.tick(Game.FPS) / 1000

            self.update_timers()
            self.all_sprites.update(dt)
            if self.player_active:
                self.ui.update()

            self.screen.blit(self.bg_surfs["bg"], (0, 0))
            self.draw_monster_floor()
            self.all_sprites.draw(self.screen)
            self.ui.draw(self.screen)
            window.flip()

    def handle_events(self) -> bool:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_ESCAPE:
            #         return False
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
