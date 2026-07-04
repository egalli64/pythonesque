"""
Master Python by making 5 games - 5: Monster battle

YouTube: https://www.youtube.com/watch?v=8OMghdHP-zs&t=32960s
GitHub: https://github.com/clear-code-projects/5games/tree/main/Monster%20battle
Google Drive: https://drive.google.com/drive/folders/15VQ37pgCwXxHZ8oBK0yc_CzKQeP2qSSl

My version: https://github.com/egalli64/pythonesque/ pygame/clear-code folder
"""

import pygame

from settings import WINDOW_HEIGHT, WINDOW_WIDTH, COLORS
from support import import_folder


class UI:
    PATH_IMAGES = "images/simple"

    @classmethod
    def load_resources(cls):
        cls.images = import_folder(cls.PATH_IMAGES)

    def __init__(self, screen, monster, player_monsters, get_input):
        self.screen = screen
        self.font = pygame.font.Font(None, 30)
        self.left = WINDOW_WIDTH / 2 - 100
        self.top = WINDOW_HEIGHT / 2 + 50
        self.monster = monster
        self.get_input = get_input

        # control
        self.general_options = ["attack", "heal", "switch", "escape"]
        self.general_index = {"col": 0, "row": 0}
        self.attack_index = {"col": 0, "row": 0}
        self.state = "general"
        self.rows, self.cols = 2, 2
        self.visible_monsters = 4
        self.player_monsters = player_monsters
        self.available_monsters = [
            monster
            for monster in self.player_monsters
            if monster != self.monster and monster.health > 0
        ]
        self.switch_index = 0

    def select(self):
        match self.state:
            case "general":
                i = self.general_index["col"]
                j = self.general_index["row"]
                self.state = self.general_options[i + j * 2]
            case "attack":
                i = self.general_index["col"]
                j = self.general_index["row"]
                attack = self.monster.abilities[i + j * 2]
                self.get_input(self.state, attack)
                self.state = "general"
            case "switch":
                data = self.available_monsters[self.switch_index]
                self.get_input(self.state, data)
                self.state = "general"

    def change_row(self, delta):
        if self.state in ("general", "attack"):
            self.general_index["row"] = (self.general_index["row"] + delta) % self.rows
        elif self.state == "switch" and self.available_monsters:
            max = len(self.available_monsters)
            self.switch_index = (self.switch_index + delta) % max

    def change_col(self, delta):
        if self.state in ("general", "attack"):
            self.general_index["col"] = (self.general_index["col"] + delta) % self.cols

    def input(self):
        if self.state == "heal":
            self.get_input("heal")
            self.state = "general"

    def escape(self):
        if self.state != "general":
            self.state = "general"
            self.general_index = {"col": 0, "row": 0}
            self.attack_index = {"col": 0, "row": 0}
            self.switch_index = 0
            return True
        else:
            return False

    def quad_select(self, screen, index, options):
        rect = pygame.FRect(self.left + 40, self.top + 60, 400, 200)
        pygame.draw.rect(screen, COLORS["white"], rect, 0, 4)
        pygame.draw.rect(screen, COLORS["gray"], rect, 4, 4)

        for col in range(self.cols):
            for row in range(self.rows):
                x = (
                    rect.left
                    + rect.width / (self.cols * 2)
                    + (rect.width / self.cols) * col
                )
                y = (
                    rect.top
                    + rect.height / (self.rows * 2)
                    + (rect.height / self.rows) * row
                )
                i = col + 2 * row
                color = (
                    COLORS["gray"]
                    if col == index["col"] and row == index["row"]
                    else COLORS["black"]
                )

                text_surf = self.font.render(options[i], True, color)
                text_rect = text_surf.get_frect(center=(x, y))
                screen.blit(text_surf, text_rect)

    def switch(self, screen):
        rect = pygame.FRect(self.left + 40, self.top - 140, 400, 400)
        pygame.draw.rect(screen, COLORS["white"], rect, 0, 4)
        pygame.draw.rect(screen, COLORS["gray"], rect, 4, 4)

        v_offset = (
            0
            if self.switch_index < self.visible_monsters
            else -(self.switch_index - self.visible_monsters + 1)
            * rect.height
            / self.visible_monsters
        )
        for i in range(len(self.available_monsters)):
            x = rect.centerx
            y = (
                rect.top
                + rect.height / (self.visible_monsters * 2)
                + rect.height / self.visible_monsters * i
                + v_offset
            )
            color = COLORS["gray"] if i == self.switch_index else COLORS["black"]
            name = self.available_monsters[i].name

            monster_image = UI.images[name]
            monster_rect = monster_image.get_frect(center=(x - 100, y))

            text_surf = self.font.render(name, True, color)
            text_rect = text_surf.get_frect(midleft=(x, y))
            if rect.collidepoint(text_rect.center):
                screen.blit(text_surf, text_rect)
                screen.blit(monster_image, monster_rect)

    def stats(self, screen):
        rect = pygame.FRect(self.left, self.top, 250, 80)
        pygame.draw.rect(screen, COLORS["white"], rect, 0, 4)
        pygame.draw.rect(screen, COLORS["gray"], rect, 4, 4)

        name_surf = self.font.render(self.monster.name, True, COLORS["black"])
        name_rect = name_surf.get_frect(
            topleft=rect.topleft + pygame.Vector2(rect.width * 0.05, 12)
        )
        screen.blit(name_surf, name_rect)

        # health bar
        health_rect = pygame.FRect(
            name_rect.left, name_rect.bottom + 10, rect.width * 0.9, 20
        )
        pygame.draw.rect(screen, COLORS["gray"], health_rect)
        self.draw_bar(screen, health_rect, self.monster.health, self.monster.max_health)

    def draw_bar(self, screen, rect, value, max_value):
        ratio = rect.width / max_value
        progress_rect = pygame.FRect(rect.topleft, (value * ratio, rect.height))
        pygame.draw.rect(screen, COLORS["red"], progress_rect)

    def update(self):
        self.input()
        self.available_monsters = [
            monster
            for monster in self.player_monsters
            if monster != self.monster and monster.health > 0
        ]

    def draw(self, screen):
        match self.state:
            case "general":
                self.quad_select(screen, self.general_index, self.general_options)
            case "attack":
                self.quad_select(screen, self.attack_index, self.monster.abilities)
            case "switch":
                self.switch(screen)

        if self.state != "switch":
            self.stats(screen)


class OpponentUI:
    def __init__(self, monster):
        self.display_surface = pygame.display.get_surface()
        self.monster = monster
        self.font = pygame.font.Font(None, 30)

    def draw(self, screen):
        # bg
        rect = pygame.FRect((0, 0), (250, 80)).move_to(
            midleft=(500, self.monster.rect.centery)
        )
        pygame.draw.rect(screen, COLORS["white"], rect, 0, 4)
        pygame.draw.rect(screen, COLORS["gray"], rect, 4, 4)

        # name
        name_surf = self.font.render(self.monster.name, True, COLORS["black"])
        name_rect = name_surf.get_frect(
            topleft=rect.topleft + pygame.Vector2(rect.width * 0.05, 12)
        )
        screen.blit(name_surf, name_rect)

        # health
        health_rect = pygame.FRect(
            name_rect.left, name_rect.bottom + 10, rect.width * 0.9, 20
        )
        ratio = health_rect.width / self.monster.max_health
        progress_rect = pygame.FRect(
            health_rect.topleft, (self.monster.health * ratio, health_rect.height)
        )
        pygame.draw.rect(screen, COLORS["gray"], health_rect)
        pygame.draw.rect(screen, COLORS["red"], progress_rect)
