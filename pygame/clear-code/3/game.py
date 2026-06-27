"""
Master Python by making 5 games - 3: Pong

YouTube: https://www.youtube.com/watch?v=8OMghdHP-zs&t=22529s
Google Drive: https://drive.google.com/drive/folders/1cczbSYaFtVaOoigmYkd9Rj1hPbYFqC1k

My version: https://github.com/egalli64/pythonesque/ pygame/clear-code folder
"""

import json

import pygame
from player import Player
from opponent import Opponent
from ball import Ball
from shadowed import Shadowed

WIN_RECT = pygame.Rect(0, 0, 1280, 720)
TITLE = "Pong"


class Game:
    FPS = 60
    COLORS = ("#002633", "#004a63")
    SCORE_FILENAME = "data/score.json"
    SCORE_X_SHIFT = 100

    @classmethod
    def load_resources(cls):
        cls._font = pygame.font.Font(None, 160)

    def __init__(self, window, screen):
        self.window = window
        self.screen = screen
        self.clock = pygame.time.Clock()

        self.all_sprites = Shadowed(self.screen)
        self.paddles = pygame.sprite.Group()
        self.player = Player(WIN_RECT, (self.all_sprites, self.paddles))
        self.ball = Ball(self.all_sprites, WIN_RECT, self.paddles, self.update_score)
        self.opponent = Opponent(self.ball, WIN_RECT, (self.all_sprites, self.paddles))

        try:
            with open(Game.SCORE_FILENAME) as f:
                self.score = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            self.score = {"player": 0, "opponent": 0}

    def run(self):
        while self.handle_events():
            dt = self.clock.tick(Game.FPS) / 1000
            self.all_sprites.update(dt)
            self.draw()

        with open(Game.SCORE_FILENAME, "w") as f:
            json.dump(self.score, f)

    def draw(self):
        self.screen.fill(Game.COLORS[0])
        pos = (WIN_RECT.midtop, WIN_RECT.midbottom)
        pygame.draw.line(self.screen, Game.COLORS[1], *pos, 6)
        self.display_score()
        self.all_sprites.draw()
        window.flip()

    def update_score(self, side):
        self.score[side] += 1

    def display_score(self):
        player = Game._font.render(str(self.score["player"]), True, Game.COLORS[1])
        player_pos = (WIN_RECT.centerx + Game.SCORE_X_SHIFT, WIN_RECT.centery)
        player_rect = player.get_frect(center=player_pos)
        self.screen.blit(player, player_rect)

        opponent = Game._font.render(str(self.score["opponent"]), True, Game.COLORS[1])
        opponent_pos = (WIN_RECT.centerx - Game.SCORE_X_SHIFT, WIN_RECT.centery)
        opponent_rect = opponent.get_frect(center=opponent_pos)
        self.screen.blit(opponent, opponent_rect)

    def handle_events(self) -> bool:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False

        keys = pygame.key.get_pressed()
        self.player.set_direction(keys[pygame.K_DOWN] - keys[pygame.K_UP])
        return True


if __name__ == "__main__":
    pygame.init()
    window = pygame.Window(TITLE, WIN_RECT.size)
    screen = window.get_surface()

    Game.load_resources()

    try:
        Game(window, screen).run()
    finally:
        pygame.time.wait(300)
        pygame.quit()
        print("Done.")
