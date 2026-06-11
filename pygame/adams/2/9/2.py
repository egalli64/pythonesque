"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Timed continous fire - Using time.get_ticks
"""

from typing import Tuple, override
import pygame

WIN_RECT = pygame.Rect(0, 0, 700, 200)
FPS = 30
TITLE = "Timed continous fire"


class Enemy(pygame.sprite.Sprite):
    MIN_X = 10
    MAX_X = WIN_RECT.right - 10
    START_POS = (MIN_X, 10)
    SPEED = pygame.Vector2(150, 0)

    def __init__(self, filename: str) -> None:
        super().__init__()
        self.image = pygame.image.load(filename).convert_alpha()
        self.rect: pygame.FRect = pygame.FRect(self.image.get_rect())
        self.rect.topleft = Enemy.START_POS
        self.direction = 1  # right

    def update(self, dt) -> None:
        newpos = self.rect.move(Enemy.SPEED * dt * self.direction)
        if newpos.left < self.MIN_X or newpos.right > self.MAX_X:
            self.direction *= -1
        else:
            self.rect = newpos


class Bullet(pygame.sprite.Sprite):
    MAX_Y = WIN_RECT.bottom - 30

    def __init__(self, filename: str, pos: Tuple) -> None:
        super().__init__()
        self.image = pygame.image.load(filename).convert_alpha()
        self.rect: pygame.FRect = pygame.FRect(self.image.get_rect())
        self.rect.center = pos
        self.direction = 1
        self.speed = pygame.math.Vector2(0, 100)

    @override
    def update(self, dt) -> None:
        self.rect.move_ip(self.speed * dt * self.direction)
        if self.rect.top > Bullet.MAX_Y:
            self.kill()


class Game(object):
    ENEMY = "../images/alien_big_1.png"
    BULLET = "../images/shoot.png"
    FIRE_INTERVAL = 333  # ms.
    BACKGROUND_COLOR = (200, 200, 200)

    def __init__(self) -> None:
        self.window = pygame.Window(TITLE, WIN_RECT.size)
        self.screen = self.window.get_surface()
        self.clock = pygame.time.Clock()

        self.enemy = Enemy(Game.ENEMY)
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.enemy)
        self.last_shot_time = pygame.time.get_ticks()

    def run(self) -> None:
        while self.handle_events():
            dt = self.clock.tick(FPS) / 1000

            self.update(dt)

            self.draw()

    def handle_events(self) -> bool:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
        return True

    def update(self, dt) -> None:
        current_time = pygame.time.get_ticks()
        if current_time - self.last_shot_time >= Game.FIRE_INTERVAL:
            pos = self.enemy.rect.move(0, 20).center
            bullet = Bullet(Game.BULLET, pos)
            self.all_sprites.add(bullet)
            self.last_shot_time = current_time

        self.all_sprites.update(dt)

    def draw(self) -> None:
        self.screen.fill(Game.BACKGROUND_COLOR)
        self.all_sprites.draw(self.screen)
        self.window.flip()


if __name__ == "__main__":
    pygame.init()

    try:
        Game().run()
    finally:
        pygame.quit()
        print("Done.")
