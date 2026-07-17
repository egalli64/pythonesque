"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

The need of having a break
"""
import pygame
from enemy import Enemy
from bullet import Bullet

WIN_RECT = pygame.Rect(0, 0, 700, 200)
FPS = 30
TITLE = "Bugged continuous fire"


class Game:
    ENEMY = "../../images/alien_big_1.png"
    BULLET = "../../images/shoot.png"
    BACKGROUND_COLOR = (200, 200, 200)

    def __init__(self) -> None:
        self.window = pygame.Window(TITLE, WIN_RECT.size)
        self.screen = self.window.get_surface()
        self.viewport = self.screen.get_rect()
        self.clock = pygame.time.Clock()

        self.enemy = Enemy(Game.ENEMY)
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.enemy)

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
        pos = self.enemy.rect.move(0, 20).center
        bullet = Bullet(Game.BULLET, pos, self.viewport.height)
        self.all_sprites.add(bullet)

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
