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
from support import import_folder, folder_importer, tile_importer, audio_importer
from monster import Creature, Monster, Opponent
from random import choice
from ui import UI, OpponentUI
from attack import AttackAnimationSprite
from timer import Timer  # type: ignore


class Game:
    FPS = 60
    BACKGROUND_FILENAME = "images/other/bg.png"
    FLOOR_FILENAME = "images/other/floor.png"

    @classmethod
    def load_resources(cls):
        cls.floor = pygame.image.load(Game.FLOOR_FILENAME)
        cls.background = pygame.image.load(Game.BACKGROUND_FILENAME)

    def __init__(self, window, screen):
        self.window = window
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.import_assets()
        # self.audio["music"].play(-1)
        self.player_active = True

        self.all_sprites = pygame.sprite.Group()

        names = ["Sparchu", "Jacana", "Plumette", "Atrox"]
        self.player_monsters = [Monster(name) for name in names]

        self.monster: Monster = self.player_monsters[0]
        self.all_sprites.add(self.monster)

        opponent_name = choice(list(MONSTER_DATA.keys()))
        self.opponent = Opponent(opponent_name, self.all_sprites)

        self.ui = UI(
            self.screen,
            self.monster,
            self.player_monsters,
            self.simple_surfs,
            self.get_input,
        )
        self.opponent_ui = OpponentUI(self.opponent)

        self.timers = {
            "player end": Timer(1000, func=self.opponent_turn),
            "opponent end": Timer(1000, func=self.player_turn),
        }

    def get_input(self, state, data=None):
        if state == "attack":
            self.apply_attack(self.opponent, data)
        elif state == "heal":
            self.monster.health += 50
            AttackAnimationSprite(
                self.monster, self.attack_frames["green"], self.all_sprites
            )
            self.audio["green"].play()
        elif state == "switch":
            self.monster.kill()
            self.monster = data
            self.all_sprites.add(self.monster)
            self.ui.monster = self.monster

        self.player_active = False
        self.timers["player end"].activate()

    def apply_attack(self, target, attack):
        attack_data = ABILITIES_DATA[attack]
        attack_multiplier = ELEMENT_DATA[attack_data["element"]][target.element]
        target.health -= attack_data["damage"] * attack_multiplier
        AttackAnimationSprite(
            target, self.attack_frames[attack_data["animation"]], self.all_sprites
        )
        self.audio[attack_data["animation"]].play()

    def opponent_turn(self):
        if self.opponent.health <= 0:
            self.player_active = True
            self.opponent.kill()
            monster_name = choice(list(MONSTER_DATA.keys()))
            self.opponent = Opponent(monster_name, self.all_sprites)
            self.opponent_ui.monster = self.opponent
        else:
            attack = choice(self.opponent.abilities)
            self.apply_attack(self.monster, attack)
            self.timers["opponent end"].activate()

    def player_turn(self):
        self.player_active = True
        if self.monster.health <= 0:
            available_monsters = [
                monster for monster in self.player_monsters if monster.health > 0
            ]
            if available_monsters:
                self.monster.kill()
                self.monster = available_monsters[0]
                self.all_sprites.add(self.monster)
                self.ui.monster = self.monster
            else:
                self.running = False

    def update_timers(self):
        for timer in self.timers.values():
            timer.update()

    def import_assets(self):
        self.simple_surfs = folder_importer("images", "simple")
        self.attack_frames = tile_importer(4, "images", "attacks")
        self.audio = audio_importer("audio")

    def draw_monster_floor(self):
        for sprite in self.all_sprites:
            if isinstance(sprite, Creature):
                floor_rect = Game.floor.get_frect(
                    center=sprite.rect.midbottom + pygame.Vector2(0, -10)
                )
                self.screen.blit(Game.floor, floor_rect)

    def run(self):
        while self.handle_events():
            dt = self.clock.tick(Game.FPS) / 1000

            self.update_timers()
            self.all_sprites.update(dt)
            if self.player_active:
                self.ui.update()

            self.screen.blit(Game.background, (0, 0))
            self.draw_monster_floor()
            self.all_sprites.draw(self.screen)
            self.ui.draw(self.screen)
            self.opponent_ui.draw(self.screen)
            window.flip()

    def handle_events(self) -> bool:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return self.ui.escape()

        return True


if __name__ == "__main__":
    pygame.init()
    window = pygame.Window(TITLE, WIN_RECT.size)
    screen = window.get_surface()

    Creature.load_resources()
    Game.load_resources()

    try:
        Game(window, screen).run()
    finally:
        pygame.quit()
        print("Done.")
