"""
Master Python by making 5 games - 2: Vampire survivor

YouTube: https://www.youtube.com/watch?v=8OMghdHP-zs&t=13523s
GitHub: https://github.com/clear-code-projects/5games/tree/main/Vampire%20survivor
Google Drive: https://drive.google.com/drive/folders/1WBhwu1yAzgmNwQ2w-SI6G8hzqwQjUN-Z

My version: https://github.com/egalli64/pythonesque/ pygame/clear-code folder
"""

import pygame
from player import Player

WIN_RECT = pygame.Rect(0, 0, 1280, 720)
TITLE = "Vampire survivor"


class Game:
    FPS = 60
    BACKGROUND_COLOR = "black"

    def __init__(self, window, screen):
        self.window = window
        self.screen = screen
        self.clock = pygame.time.Clock()

        self.all_sprites = pygame.sprite.Group()

        self.player = Player(WIN_RECT.center, self.all_sprites)

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

        keys = pygame.key.get_pressed()  # continuous events handling

        x = keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]
        y = keys[pygame.K_DOWN] - keys[pygame.K_UP]
        self.player.set_direction(x, y)

        return True


if __name__ == "__main__":
    pygame.init()
    window = pygame.Window(TITLE, WIN_RECT.size)
    screen = window.get_surface()

    Player.load_resources()

    try:
        Game(window, screen).run()
    finally:
        pygame.quit()
        print("Done.")
