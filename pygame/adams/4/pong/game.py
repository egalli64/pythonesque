"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Pong game
"""
import pygame
from background import Background
from pause import Pause
from help import Help
from paddle import Paddle
from ball import Ball
from score import Score
from events import Events

WIN_SIZE = (1000, 600)
TITLE = "Pong"
FPS = 60


class Game:
    def __init__(self, window: pygame.Window, screen: pygame.Surface):
        self.window = window
        self.screen = screen

        viewport = screen.get_rect()
        self.background = Background(viewport)
        self.all_sprites = pygame.sprite.Group()

        self.paddles = (Paddle("left", viewport), Paddle("right", viewport))
        self.all_sprites.add(self.paddles)
        self.ball = Ball(viewport, self.all_sprites)
        self.score = Score(self.all_sprites)
        self.running = True
        self.pausing = False
        self.helping = False
        self.pause = Pause(viewport)
        self.help = Help(viewport)

    def run(self):
        clock = pygame.time.Clock()

        while self.handle_events():
            dt = clock.tick(FPS) / 1000
            self.update(dt)
            self.draw()

    def update(self, dt):
        if not (self.pausing or self.helping):
            self.check_collision()
            for paddle in self.paddles:
                paddle.auto_move(self.ball.rect.centery)
            self.all_sprites.update(dt, action="move")

    def draw(self):
        self.background.draw(self.screen)
        self.all_sprites.draw(self.screen)
        if self.pausing:
            self.pause.draw(self.screen)
        elif self.helping:
            self.help.draw(self.screen)
        self.window.flip()

    def handle_events(self) -> bool:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
                elif event.key == pygame.K_F2:
                    self.ball.toggle_sound_effect()
                elif event.key == pygame.K_1:
                    self.paddles[0].toggle_auto()
                elif event.key == pygame.K_2:
                    self.paddles[1].toggle_auto()
                elif event.key == pygame.K_p:
                    if not self.helping:
                        self.pausing = not self.pausing
                elif event.key == pygame.K_h:
                    if not self.pausing:
                        self.helping = not self.helping
            elif event.type == Events.POINT_FOR:
                self.score.point_for(event.player)

        keys = pygame.key.get_pressed()
        self.paddles[0].set_direction(keys[pygame.K_s] - keys[pygame.K_w])
        self.paddles[1].set_direction(keys[pygame.K_DOWN] - keys[pygame.K_UP])

        return True

    def check_collision(self):
        if pygame.sprite.collide_rect(self.ball, self.paddles[0]):
            self.ball.horizontal_flip()
            self.ball.rect.left = self.paddles[0].rect.right + 1
        elif pygame.sprite.collide_rect(self.ball, self.paddles[1]):
            self.ball.horizontal_flip()
            self.ball.rect.right = self.paddles[1].rect.left - 1


# noinspection DuplicatedCode
if __name__ == "__main__":
    pygame.init()
    pg_window = pygame.Window(TITLE, WIN_SIZE)
    pg_screen = pg_window.get_surface()

    Ball.load_resources()
    Paddle.load_resources()

    try:
        Game(pg_window, pg_screen).run()
    finally:
        pygame.quit()
        print("Done.")
