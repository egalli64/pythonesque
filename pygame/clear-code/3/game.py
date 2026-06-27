"""
Master Python by making 5 games - 3: Pong

YouTube: https://www.youtube.com/watch?v=8OMghdHP-zs&t=22529s
Google Drive: https://drive.google.com/drive/folders/1cczbSYaFtVaOoigmYkd9Rj1hPbYFqC1k

My version: https://github.com/egalli64/pythonesque/ pygame/clear-code folder
"""

import pygame
from player import Player
from opponent import Opponent
from ball import Ball

WIN_RECT = pygame.Rect(0, 0, 1280, 720)
TITLE = "Pong"


class Game:
    FPS = 60
    BACKGROUND_COLOR = "#002633"

    def __init__(self, window, screen):
        self.window = window
        self.screen = screen
        self.clock = pygame.time.Clock()

        self.all_sprites = pygame.sprite.Group()
        self.paddles = pygame.sprite.Group()
        self.player = Player(WIN_RECT, (self.all_sprites, self.paddles))
        self.ball = Ball(self.all_sprites, WIN_RECT, self.paddles)
        self.opponent = Opponent(self.ball, WIN_RECT, (self.all_sprites, self.paddles))

    def run(self):
        while self.handle_events():
            dt = self.clock.tick(Game.FPS) / 1000

            self.all_sprites.update(dt)

            self.screen.fill(Game.BACKGROUND_COLOR)
            self.all_sprites.draw(self.screen)
            window.flip()

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

    try:
        Game(window, screen).run()
    finally:
        pygame.time.wait(300)
        pygame.quit()
        print("Done.")
